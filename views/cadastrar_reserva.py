import tkinter as tk

from banco_de_dados import BancoDeDados
from models import Reserva, Tecnico
from views.janela_base import CadastroBase
import csv


class CadastrarReserva(CadastroBase):
    def __init__(self, janela_criadora=None, reserva: Reserva = None):
        CadastroBase.__init__(self, 'Cadastro de Reservas', 'reservas.csv', altura=450)

        self.altera_cadastro = reserva
        self.janela_criadora = janela_criadora
        self.bd_tecnicos = BancoDeDados('tecnicos.csv', self.cria_tecnico)

        # cria variáveis dos campos:
        self.id_reserva = tk.StringVar()
        self.id_ferramenta = tk.StringVar()
        self.id_tecnico = tk.StringVar()
        self.data_reserva = tk.StringVar()
        self.data_entrega = tk.StringVar()
        self.status = tk.StringVar()

        if reserva is not None:
            self.id_reserva.set(reserva.id_reserva)
            self.id_ferramenta.set(reserva.id_ferramenta)
            self.id_tecnico.set(reserva.id_tecnico)
            self.data_reserva.set(reserva.data_reserva)
            self.data_entrega.set(reserva.data_entrega)
            self.status.set(reserva.status)

        self.cria_elementos()

    def cria_elementos(self):

        def cria_lista_opcoes_tecnicos():
            id_cpf = []
            nome = []
            sobrenome = []
            for tecnico in self.bd_tecnicos.linhas:
                id_cpf.append(tecnico.id_cpf)
                nome.append(tecnico.nome)
                sobrenome.append(tecnico.sobrenome)
            opcoes_tecnico = []
            index = 0
            for i in id_cpf:
                conjunto = [id_cpf[index], nome[index], sobrenome[index]]
                opcoes_tecnico.append(' '.join(conjunto))
                index += 1
            return opcoes_tecnico

        opcoes_tecnico = cria_lista_opcoes_tecnicos()

        self.adiciona_campo('Identificação da Reserva', self.id_reserva)
        self.adiciona_campo('Identificação da Ferramenta', self.id_ferramenta)
        self.adiciona_dropdown('Identificação do Técnico', self.id_tecnico, opcoes_tecnico)
        self.adiciona_campo('Data da reserva', self.data_reserva)
        self.adiciona_campo('Data da entrega', self.data_entrega)
        self.adiciona_campo('Status da reserva', self.status)

        texto_cadastro = 'Cadastrar' if self.altera_cadastro is None else 'Alterar cadastro'
        cadastra_button = tk.Button(self.janela, text=texto_cadastro, command=self.confirma_cadastro)
        cadastra_button.grid(column=0, row=self.linha + 2, padx=5, pady=8, columnspan=2)

    def cria_objeto(self, dicionario):
        return Reserva(**dicionario)

    def cria_tecnico(self, dicionario):
        return Tecnico(**dicionario)

    def confirma_cadastro(self):
        if not self.valida_id():
            return

        reserva = Reserva(self.id_reserva.get(),
                          self.id_ferramenta.get(),
                          self.id_tecnico.get(),
                          self.data_reserva.get(),
                          self.data_entrega.get(),
                          self.status.get())

        self.salva_cadastro(reserva)

    def valida_id(self):
        id_reserva = self.id_reserva.get()
        if not id_reserva.isdigit():
            self.abre_popup('Valor inválido', 'O campo "Id Reserva" deve conter apenas números.')
            return False

        return True

    def limpa_campos(self):
        self.id_reserva.set('')
        self.id_ferramenta.set('')
        self.id_tecnico.set('')
        self.data_reserva.set('')
        self.data_entrega.set('')
        self.status.set('')
