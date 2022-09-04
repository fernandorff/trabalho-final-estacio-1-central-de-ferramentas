import tkinter as tk
from tkinter import *
from tkinter import ttk
from banco_de_dados import BancoDeDados
from tkcalendar import *
from datetime import date


class JanelaBase(Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        # Inicializa variáveis:
        self.janela_criadora = None
        self.popUp = None

    def define_dimensões(self, janela, largura=800, altura=600):
        # pega as dimensões da tela:
        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()
        # calcula o ponto central:
        centro_x = int(screen_width / 2 - largura / 2)
        centro_y = int(screen_height / 2 - altura / 2)

        # define a posição da janela para o centro da tela:
        janela.geometry(f'{largura}x{altura}+{centro_x}+{centro_y}')

    def abre_popup(self, titulo, mensagem):
        if self.popUp is not None:
            self.popUp.destroy()

        self.popUp = PopUp(titulo, mensagem)


class PopUp(JanelaBase):
    def __init__(self, título, mensagem):
        JanelaBase.__init__(self)

        self.janela = Toplevel(self)
        self.janela.title(título)
        self.define_dimensões(self.janela, 300, 100)

        label = tk.Label(self.janela, text=mensagem)
        label.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )

        ok_button = tk.Button(
            self.janela,
            text='Ok',
            command=lambda: self.janela.destroy()
        )

        ok_button.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )


class CadastroBase(JanelaBase):
    def __init__(self, título, arquivo_bd, largura=400, altura=270):
        JanelaBase.__init__(self)

        self.altera_cadastro = None

        self.janela = Toplevel(self)
        self.janela.title(título)
        self.define_dimensões(self.janela, largura, altura)

        # configura a grid:
        self.janela.columnconfigure(0, weight=1)
        self.janela.columnconfigure(1, weight=3)

        # inicializa o contador de linhas:
        self.linha = 0

        # banco de dados:
        self.bd = BancoDeDados(arquivo_bd, self.cria_objeto)

    def adiciona_campo(self, titulo, variavel):
        label = tk.Label(self.janela, text=titulo)
        label.grid(column=0, row=self.linha, sticky=tk.W, padx=5, pady=8)

        entry = tk.Entry(self.janela, textvariable=variavel)
        entry.grid(column=1, row=self.linha, sticky=tk.EW, padx=10, pady=5)

        self.linha += 1
        return entry

    def adiciona_dropdown(self, titulo, variavel, opcoes):
        label = tk.Label(self.janela, text=titulo)
        label.grid(column=0, row=self.linha, sticky=tk.W, padx=5, pady=8)

        entry = tk.OptionMenu(self.janela, variavel, *opcoes)
        entry.grid(column=1, row=self.linha, sticky=tk.EW, padx=10, pady=5)

        self.linha += 1
        return entry

    def adiciona_calendario(self):
        entry = Calendar(self.janela, selectmode="day", year=date.today().year, month=date.today().month,
                         day=date.today().day)
        entry.grid(column=1, row=self.linha, sticky=tk.EW, padx=10, pady=5)

        def grab_date():
            my_label.config(text="Date is " + entry.get_date())

        my_button = Button(self.janela, text="GEt Date", command=grab_date)

        my_label = Label(self.janela, text="")

        self.linha += 1
        return entry

    def salva_cadastro(self, objeto):
        if self.altera_cadastro is not None:
            self.bd.altera_linha(objeto)
            self.bd.salvar()
            self.abre_popup('Sucesso', 'Cadastro alterado com sucesso.')

            if self.janela_criadora is not None:
                self.janela_criadora.cadastro_atualizado()
        else:
            self.bd.adiciona_linha(objeto)
            self.bd.salvar()
            self.limpa_campos()
            self.abre_popup('Sucesso', 'Cadastro realizado com sucesso.')


class ListagemBase(JanelaBase):
    def __init__(self, título, arquivo_bd, largura=600, altura=400):
        JanelaBase.__init__(self)

        self.janela_altera_cadastro = None
        self.tabela = None
        self.janela = Toplevel(self)
        self.janela.title(título)
        self.define_dimensões(self.janela, largura, altura)

        # configura item selecionado:
        self.id_selecionado = None
        self.linha_selecionada = None

        # configura a grid:
        self.janela.columnconfigure(0, weight=1)
        self.janela.columnconfigure(1, weight=3)

        # elementos:
        self.excluir_button = None
        self.alterar_button = None

        # banco de dados:
        self.bd = BancoDeDados(arquivo_bd, self.cria_objeto)

        self.cria_elementos()

    def cadastro_atualizado(self):
        self.janela_altera_cadastro.destroy()
        self.janela_altera_cadastro = None
        self.bd.atualiza()

        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        self.popula_tabela()

    def cria_elementos(self):
        # scrollbar
        vscroll = Scrollbar(self.janela)
        vscroll.pack(side=RIGHT, fill=Y)

        hscroll = Scrollbar(self.janela, orient=HORIZONTAL)
        hscroll.pack(side=BOTTOM, fill=X)

        self.tabela = ttk.Treeview(self.janela,
                                   height=20,
                                   yscrollcommand=vscroll.set,
                                   xscrollcommand=hscroll.set,
                                   selectmode="browse")
        self.tabela.bind('<ButtonRelease-1>', self.seleciona_item)

        vscroll.config(command=self.tabela.yview)
        hscroll.config(command=self.tabela.xview)

        footer = Frame(self.janela)
        footer.pack(side=BOTTOM)

        self.popula_tabela()

        self.excluir_button = tk.Button(footer, text="Excluir selecionado", command=self.exclui_selecionado)
        self.alterar_button = tk.Button(footer, text="Alterar selecionado", command=self.altera_selecionado)

    def seleciona_item(self, evt):
        seleção = self.tabela.selection()

        if len(seleção) == 0:
            self.limpa_seleção()
        else:
            self.linha_selecionada = seleção[0]
            self.id_selecionado = self.tabela.item(self.linha_selecionada)['values'][0]
            self.excluir_button.pack(side=LEFT)
            self.alterar_button.pack(side=RIGHT)

    def exclui_selecionado(self):
        if self.linha_selecionada is None or self.id_selecionado is None:
            raise Exception('Nenhum item selecionado')

        id_campo = self.tabela['columns'][0]
        self.bd.remove_linha(id_campo, self.id_selecionado)
        self.bd.salvar()

        self.tabela.delete(self.linha_selecionada)
        self.limpa_seleção()

    def altera_selecionado(self):
        if self.linha_selecionada is None or self.id_selecionado is None:
            raise Exception('Nenhum item selecionado')

        id_campo = self.tabela['columns'][0]
        linha = self.bd.encontra_linha(id_campo, self.id_selecionado)
        self.abre_alterar_cadastro(linha)

    def limpa_seleção(self):
        self.id_selecionado = None
        self.linha_selecionada = None

        # Esconde botões de excluir e alterar:
        self.excluir_button.pack_forget()
        self.alterar_button.pack_forget()
