import tkinter as tk
from tkinter import *

from views.cadastrar_reserva import CadastrarReserva
from views.janela_base import JanelaBase
from views.listar_reservas import ListarReservas
from views.listar_tecnicos import ListarTécnicos
from views.cadastrar_tecnico import CadastrarTécnico
from views.listar_ferramentas import ListarFerramentas
from views.cadastrar_ferramenta import CadastrarFerramenta


class MenuPrincipal(JanelaBase):
    def __init__(self):
        JanelaBase.__init__(self)

        # Título da janela:
        self.master.title('Menu Principal')
        self.master['bg'] = '#BFE0D6'

        # Ajusta tamanho e posição da tela:
        self.define_dimensões(self.master)

        # Inicializa variáveis:
        self.janela = None

        self.cria_elementos()

    def cria_elementos(self):
        linha = 0
        frame = Frame(self.master, bg='#BFE0D6')

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
        lista_ferramenta_button = tk.Button(
            frame,
            text='Listar Ferramentas',
            command=lambda: self.abre_lista_ferramenta()
        )
        lista_ferramenta_button.grid(column=0, row=linha, sticky=tk.EW, padx=10, pady=10, ipadx=10, ipady=10)

        # cadastro ferramentas:
        cadastro_técnico_button = tk.Button(
            frame,
            text='Cadastrar nova Ferramenta',
            command=lambda: self.abre_cadastro_ferramenta()
        )
        cadastro_técnico_button.grid(column=1, row=linha, sticky=tk.EW, padx=10, pady=5, ipadx=10, ipady=10)
        linha += 1

        # lista reservas:
        lista_ferramenta_button = tk.Button(
            frame,
            text='Listar Reservas',
            command=lambda: self.abre_lista_reserva()
        )
        lista_ferramenta_button.grid(column=0, row=linha, sticky=tk.EW, padx=10, pady=10, ipadx=10, ipady=10)

        # cadastro reservas:
        cadastro_reserva_button = tk.Button(
            frame,
            text='Cadastrar nova Reserva',
            command=lambda: self.abre_cadastro_reserva()
        )
        cadastro_reserva_button.grid(column=1, row=linha, sticky=tk.EW, padx=10, pady=5, ipadx=10, ipady=10)
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
        self.janela = ListarTécnicos()

    def abre_cadastro_técnico(self):
        self.janela = CadastrarTécnico()

    def abre_lista_ferramenta(self):
        self.janela = ListarFerramentas()

    def abre_cadastro_ferramenta(self):
        self.janela = CadastrarFerramenta()

    def abre_cadastro_reserva(self):
        self.janela = CadastrarReserva()

    def abre_lista_reserva(self):
        self.janela = ListarReservas()
