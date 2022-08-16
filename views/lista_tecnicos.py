import tkinter as tk
from tkinter import ttk
from tkinter import *
from models import Tecnico
from views.janela_base import JanelaBase
from banco_de_dados import BancoDeDados


class ListaTécnicos(JanelaBase):
    def __init__(self):
        JanelaBase.__init__(self)

        self.janela = Toplevel(self)
        self.janela.title("Cadastro de Técnicos")
        self.define_dimensões(self.janela, 600, 400)

        # configura a grid:
        self.janela.columnconfigure(0, weight=1)
        self.janela.columnconfigure(1, weight=3)

        # inicializa o contador de linhas:
        self.colunas = 0
        self.linha = 0

        # banco de dados:
        self.bd = BancoDeDados('tecnicos.csv', self.cria_tecnico)

        self.cria_elementos()

    def cria_tecnico(self, dicionario):
        return Tecnico(**dicionario)

    def cria_elementos(self):
        # scrollbar
        vscroll = Scrollbar(self.janela)
        vscroll.pack(side=RIGHT, fill=Y)

        hscroll = Scrollbar(self.janela, orient=HORIZONTAL)
        hscroll.pack(side=BOTTOM, fill=X)

        tabela = ttk.Treeview(self.janela, height=20, yscrollcommand=vscroll.set, xscrollcommand=hscroll.set)

        vscroll.config(command=tabela.yview)
        hscroll.config(command=tabela.xview)

        # define as colunas
        tabela['columns'] = ('id_cpf', 'nome', 'sobrenome', 'telefone', 'turno', 'equipe')

        # format our column
        tabela.column("#0", width=0, stretch=NO)
        tabela.column("id_cpf", anchor=CENTER, width=95, stretch=YES)
        tabela.column("nome", anchor=CENTER, width=95, stretch=YES)
        tabela.column("sobrenome", anchor=CENTER, width=95, stretch=YES)
        tabela.column("telefone", anchor=CENTER, width=95, stretch=YES)
        tabela.column("turno", anchor=CENTER, width=95, stretch=YES)
        tabela.column("equipe", anchor=CENTER, width=95, stretch=YES)

        # Create Headings
        tabela.heading("id_cpf", text="Cpf", anchor=CENTER)
        tabela.heading("nome", text="Nome", anchor=CENTER)
        tabela.heading("sobrenome", text="Sobrenome", anchor=CENTER)
        tabela.heading("telefone", text="Telefone", anchor=CENTER)
        tabela.heading("turno", text="Turno", anchor=CENTER)
        tabela.heading("equipe", text="Equipe", anchor=CENTER)

        for objeto in self.bd.linhas:
            tabela.insert(parent='', index='end',
                          values=(objeto.id_cpf, objeto.nome, objeto.sobrenome, objeto.telefone, objeto.turno, objeto.equipe))
            self.linha += 1

        tabela.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )
