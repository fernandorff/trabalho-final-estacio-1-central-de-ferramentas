import tkinter as tk
from datetime import datetime

from banco_de_dados import BancoDeDados
from models import Reserva, Tecnico, Ferramenta
from views.cadastro_base import CadastroBase

class CadastrarReserva(CadastroBase):

    def __init__(self, janela_criadora=None, reserva: Reserva = None):
        CadastroBase.__init__(self, 'Cadastro de Reservas', 'reservas.csv', altura=450)

        self.altera_cadastro = reserva
        self.janela_criadora = janela_criadora
        self.bd_tecnicos = BancoDeDados('tecnicos.csv', self.cria_tecnico)
        self.bd_reserva = BancoDeDados('reservas.csv', self.cria_objeto)
        self.bd_ferramentas = BancoDeDados('ferramentas.csv', self.cria_ferramenta)

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

        def cria_lista_opcoes_ferramentas():
            id_ferramenta = []
            modelo = []
            fabricante = []
            for ferramenta in self.bd_ferramentas.linhas:
                id_ferramenta.append(ferramenta.id_ferramenta)
                modelo.append(ferramenta.modelo)
                fabricante.append(ferramenta.fabricante)
            opcoes_ferramenta = []
            index = 0
            for i in id_ferramenta:
                conjunto = [id_ferramenta[index], modelo[index], fabricante[index]]
                opcoes_ferramenta.append(' '.join(conjunto))
                index += 1
            return opcoes_ferramenta

        opcoes_ferramenta = cria_lista_opcoes_ferramentas()
        opcoes_tecnico = cria_lista_opcoes_tecnicos()
        opcoes_status = ['Em andamento', 'Em atraso', 'Concluído']

        self.adiciona_campo('Identificação da Reserva', self.id_reserva)
        self.adiciona_campo('Data da reserva (Formato: DD/MM/AAAA)', self.data_reserva)
        self.adiciona_campo('Data da entrega (Formato: DD/MM/AAAA)', self.data_entrega)
        self.adiciona_dropdown('Identificação da Ferramenta', self.id_ferramenta, opcoes_ferramenta)
        self.adiciona_dropdown('Identificação do Técnico', self.id_tecnico, opcoes_tecnico)
        self.adiciona_dropdown('Status da reserva', self.status, opcoes_status)

        texto_cadastro = 'Cadastrar' if self.altera_cadastro is None else 'Alterar cadastro'
        cadastra_button = tk.Button(self.janela, text=texto_cadastro, command=self.confirma_cadastro)
        cadastra_button.grid(column=0, row=self.linha + 2, padx=5, pady=8, columnspan=2)

    def cria_objeto(self, dicionario):
        return Reserva(**dicionario)

    def cria_ferramenta(self, dicionario):
        return Ferramenta(**dicionario)

    def cria_tecnico(self, dicionario):
        return Tecnico(**dicionario)

    def confirma_cadastro(self):
        if not self.valida_id():
            return
        if not self.valida_data(self.data_reserva.get()):
            return
        if not self.valida_data(self.data_entrega.get()):
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
            self.abre_popup('ID inválido', 'O campo "Id. da Reserva" deve conter apenas números.')
            return False
        # for reserva in self.bd_reserva.linhas:
        #     if self.id_reserva.get() == reserva.id_reserva:
        #         self.abre_popup('ID inválido', 'O valor inserido já existe.')
        #         return False

        return True

    def valida_data(self, data_recebida):

        formato = "%d/%m/%Y"
        try:
            valid = bool(datetime.strptime(data_recebida, formato))
        except ValueError:
            valid = False

        if not valid:
            self.abre_popup('DATA inválida', 'O campo Data deve estar no formato DD/MM/AAAA.')
            return False

        return True

    def limpa_campos(self):
        self.id_reserva.set('')
        self.id_ferramenta.set('')
        self.id_tecnico.set('')
        self.data_reserva.set('')
        self.data_entrega.set('')
        self.status.set('')
