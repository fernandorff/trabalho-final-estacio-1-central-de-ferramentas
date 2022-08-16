import tkinter as tk
from tkinter import *
from views.janela_base import JanelaBase
from views.lista_tecnicos import ListaTécnicos
from views.cadastro_tecnico import CadastroDeTécnico


class MenuPrincipal(JanelaBase):
    def __init__(self):
        JanelaBase.__init__(self)

        # Título da janela:
        self.master.title('Menu Principal')
        self.master['bg'] = '#F2B33D'

        # Ajusta tamanho e posição da tela:
        self.define_dimensões(self.master)

        # Inicializa variáveis:
        self.janela = None

        self.cria_elementos()

    def cria_elementos(self):
        linha = 0
        frame = Frame(self.master, bg='#F2B33D')

        label = tk.Label(frame, text='Trabalho de Certificação Mundo 1', font=('Helvetica bold', 20))
        label.config(bg='#F2B33D')
        label.grid(column=0, row=linha, columnspan=2, rowspan=2, sticky=tk.EW, padx=5, pady=8, )
        linha += 2

        # lista técnicos:
        lista_técnico_button = tk.Button(
            frame,
            text='Listar Técnicos',
            command=lambda: self.abre_lista_técnico()
        )
        lista_técnico_button.grid(column=0, row=linha, sticky=tk.EW, padx=10, pady=10, ipadx=10, ipady=10)

        # cadastro técnico:
        cadastro_técnico_button = tk.Button(
            frame,
            text='Cadastrar novo Técnico',
            command=lambda: self.abre_cadastro_técnico()
        )
        cadastro_técnico_button.grid(column=1, row=linha, sticky=tk.EW, padx=10, pady=5, ipadx=10, ipady=10)
        linha += 1

        # lista ferramentas:
        lista_técnico_button = tk.Button(
            frame,
            text='Listar Ferramentas',
            command=lambda: self.abre_lista_técnico()
        )
        lista_técnico_button.grid(column=0, row=linha, sticky=tk.EW, padx=10, pady=10, ipadx=10, ipady=10)

        # cadastro ferramentas:
        cadastro_técnico_button = tk.Button(
            frame,
            text='Cadastrar nova Ferramenta',
            command=lambda: self.abre_cadastro_técnico()
        )
        cadastro_técnico_button.grid(column=1, row=linha, sticky=tk.EW, padx=10, pady=5, ipadx=10, ipady=10)
        linha += 2

        # sair:
        sair_button = tk.Button(
            frame,
            text='Sair',
            command=lambda: self.master.quit()
        )
        sair_button.grid(column=0, row=linha, padx=10, pady=30, columnspan=2, ipadx=10, ipady=10)

        frame.pack(
            padx=10,
            pady=10,
            expand=True
        )

    def abre_lista_técnico(self):
        self.janela = ListaTécnicos()

    def abre_cadastro_técnico(self):
        self.janela = CadastroDeTécnico()
