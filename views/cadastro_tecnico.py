import tkinter as tk
from tkinter import *
from models import Tecnico
from views.janela_base import JanelaBase
from banco_de_dados import BancoDeDados


class CadastroDeTécnico(JanelaBase):
    def __init__(self):
        JanelaBase.__init__(self)

        self.janela = Toplevel(self)
        self.janela.title("Cadastro de Técnicos")
        self.define_dimensões(self.janela, 400, 270)

        # configura a grid:
        self.janela.columnconfigure(0, weight=1)
        self.janela.columnconfigure(1, weight=3)

        # inicializa o contador de linhas:
        self.linha = 0

        # cria variáveis dos campos:
        self.cpf = tk.StringVar()
        self.nome = tk.StringVar()
        self.sobrenome = tk.StringVar()
        self.telefone = tk.StringVar()
        self.equipe = tk.StringVar()
        self.turno = tk.StringVar()

        self.cria_elementos()

        # banco de dados:
        self.bd = BancoDeDados('tecnicos.csv', self.cria_tecnico)

    def cria_elementos(self):
        self.adiciona_campo('CPF:', self.cpf)
        self.adiciona_campo('Nome:', self.nome)
        self.adiciona_campo('Sobrenome:', self.sobrenome)
        self.adiciona_campo('Telefone:', self.telefone)
        self.adiciona_campo('Turno:', self.turno)
        self.adiciona_campo('Equipe:', self.equipe)

        cadastra_button = tk.Button(self.janela, text="Cadastrar", command=self.cadastra_técnico)
        cadastra_button.grid(column=0, row=self.linha + 2, padx=5, pady=8, columnspan=2)

    def adiciona_campo(self, título, variável):
        label = tk.Label(self.janela, text=título)
        label.grid(column=0, row=self.linha, sticky=tk.W, padx=5, pady=8)

        entry = tk.Entry(self.janela, textvariable=variável)
        entry.grid(column=1, row=self.linha, sticky=tk.EW, padx=10, pady=5)

        self.linha += 1

    def cria_tecnico(self, dicionario):
        return Tecnico(**dicionario)

    def cadastra_técnico(self):
        tecnico = Tecnico(self.cpf.get(),
                          self.nome.get(),
                          self.sobrenome.get(),
                          self.telefone.get(),
                          self.turno.get(),
                          self.equipe.get())

        self.bd.adiciona_linha(tecnico)

        # TODO: realizar validações dos campos
        self.bd.salvar()
        self.limpa_campos()
        self.abre_popup('Sucesso', 'Cadastro realizado com sucesso.')

    def limpa_campos(self):
        self.cpf.set('')
        self.nome.set('')
        self.sobrenome.set('')
        self.telefone.set('')
        self.turno.set('')
        self.equipe.set('')