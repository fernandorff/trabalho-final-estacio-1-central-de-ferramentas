import tkinter as tk
from tkinter import Toplevel, Scrollbar, RIGHT, Y, HORIZONTAL, BOTTOM, X, ttk, Frame, LEFT
from banco_de_dados import BancoDeDados
from relatorio import Relatorio
from views.janela_base import JanelaBase
from tkinter.filedialog import *
import subprocess, os, platform


class ListagemBase(JanelaBase):

    def __init__(self, título, caminho, largura=600, altura=400):
        JanelaBase.__init__(self)

        self.caminho = caminho
        self.título = título
        self.file_names = None
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
        self.bd = BancoDeDados(f'{caminho}.csv', self.cria_objeto)

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
                                   selectmode='browse')
        self.tabela.bind('<ButtonRelease-1>', self.seleciona_item)

        vscroll.config(command=self.tabela.yview)
        hscroll.config(command=self.tabela.xview)

        footer = Frame(self.janela)
        footer.pack(side=BOTTOM)

        self.popula_tabela()

        tk.Button(footer, text='Gerar relatório',
                  command=self.gera_relatorio,
                  relief='solid',
                  bg='#21BBEF',
                  fg='white',
                  highlightcolor="#37d3ff",
                  borderwidth=1,
                  font=15).pack(side=BOTTOM)

        self.excluir_button = tk.Button(footer, text='Excluir selecionado',
                                        command=self.exclui_selecionado,
                                        relief='solid',
                                        bg='#21BBEF',
                                        fg='white',
                                        highlightcolor="#37d3ff",
                                        borderwidth=1,
                                        font=15)
        self.alterar_button = tk.Button(footer, text='Alterar selecionado',
                                        command=self.altera_selecionado,
                                        relief='solid',
                                        bg='#21BBEF',
                                        fg='white',
                                        highlightcolor="#37d3ff",
                                        borderwidth=1,
                                        font=15)

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

    def gera_relatorio(self):
        relatorio = Relatorio(f'Relatório - {self.título}')
        relatorio.alias_nb_pages()
        relatorio.add_page()

        colunas = self.tabela['columns']
        lista = [self.tabela.heading(c)['text'] for c in colunas]

        relatorio.adiciona_colunas(lista)

        num_colunas = len(colunas)
        for linha in self.tabela.get_children():
            values = self.tabela.item(linha)['values']

            for i in range(num_colunas):
                relatorio.adiciona_celula(str(values[i]))

            relatorio.quebra_linha()

        path = askdirectory(initialdir="/",
                            title="Escolha a pasta de destino")
        path = f'{path}/relatorio-{self.caminho}.pdf'
        relatorio.output(path)

        # abre o arquivo gerado:
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', path))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(path)
        else:  # linux
            subprocess.call(('xdg-open', path))
