import tkinter as tk
from models import Reserva
from views.janela_base import CadastroBase


class CadastrarReserva(CadastroBase):
    def __init__(self):
        CadastroBase.__init__(self, 'Cadastro de Reservas', 'reservas.csv', altura=280)

        # cria variáveis dos campos:
        self.id_reserva = tk.StringVar()
        self.id_ferramenta = tk.StringVar()
        self.id_tecnico = tk.StringVar()
        self.data_reserva = tk.StringVar()
        self.data_entrega = tk.StringVar()
        self.status = tk.StringVar()

        self.cria_elementos()

    def cria_elementos(self):
        self.adiciona_campo('Identificação da Reserva', self.id_reserva)
        self.adiciona_campo('Identificação da Ferramenta', self.id_ferramenta)
        self.adiciona_campo('Identificação do Técnico', self.id_tecnico)
        self.adiciona_campo('Data da reserva', self.data_reserva)
        self.adiciona_campo('Data da entrega', self.data_entrega)
        self.adiciona_campo('Status da reserva', self.status)

        cadastra_button = tk.Button(self.janela, text="Cadastrar", command=self.confirma_cadastro)
        cadastra_button.grid(column=0, row=self.linha + 2, padx=5, pady=8, columnspan=2)

    def cria_objeto(self, dicionario):
        return Reserva(**dicionario)

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