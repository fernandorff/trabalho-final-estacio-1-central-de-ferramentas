import tkinter as tk
from tkinter import *
from tkinter import ttk
from banco_de_dados import BancoDeDados


class JanelaBase(Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        # Inicializa variáveis:
        self.popUp = None

    def define_dimensões(self, janela, largura=800, altura=600):
        # pega as dimensões da tela:
        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()
        # find the center point
        centro_x = int(screen_width / 2 - largura / 2)
        centro_y = int(screen_height / 2 - altura / 2)

        # define a posição da janela para o centro da tela:
        janela.geometry(f'{largura}x{altura}+{centro_x}+{centro_y}')

    def abre_popup(self, titulo, mensagem):
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

    def adiciona_campo(self, título, variável):
        label = tk.Label(self.janela, text=título)
        label.grid(column=0, row=self.linha, sticky=tk.W, padx=5, pady=8)

        entry = tk.Entry(self.janela, textvariable=variável)
        entry.grid(column=1, row=self.linha, sticky=tk.EW, padx=10, pady=5)

        self.linha += 1

    def salva_cadastro(self, objeto):
        self.bd.adiciona_linha(objeto)
        self.bd.salvar()
        self.limpa_campos()
        self.abre_popup('Sucesso', 'Cadastro realizado com sucesso.')


class ListagemBase(JanelaBase):
    def __init__(self, título, arquivo_bd, largura=600, altura=400):
        JanelaBase.__init__(self)

        self.tabela = None
        self.janela = Toplevel(self)
        self.janela.title(título)
        self.define_dimensões(self.janela, largura, altura)

        # configura a grid:
        self.janela.columnconfigure(0, weight=1)
        self.janela.columnconfigure(1, weight=3)

        # inicializa o contador de linhas:
        self.colunas = 0
        self.linha = 0

        # banco de dados:
        self.bd = BancoDeDados(arquivo_bd, self.cria_objeto)

    def cria_elementos(self):
        # scrollbar
        vscroll = Scrollbar(self.janela)
        vscroll.pack(side=RIGHT, fill=Y)

        hscroll = Scrollbar(self.janela, orient=HORIZONTAL)
        hscroll.pack(side=BOTTOM, fill=X)

        self.tabela = ttk.Treeview(self.janela, height=20, yscrollcommand=vscroll.set, xscrollcommand=hscroll.set)

        vscroll.config(command=self.tabela.yview)
        hscroll.config(command=self.tabela.xview)