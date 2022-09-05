import tkinter as tk
from datetime import date
from tkinter import Toplevel, Button, Label

from tkcalendar import Calendar

from banco_de_dados import BancoDeDados
from views.janela_base import JanelaBase


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

        entry = 1

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
