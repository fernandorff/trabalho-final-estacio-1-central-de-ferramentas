from tkinter import *
from models import Reserva
from views.janela_base import ListagemBase


class ListarReservas(ListagemBase):
    def __init__(self):
        ListagemBase.__init__(self, 'Listagem de Reservas', 'reservas.csv')

        self.cria_elementos()

    def cria_objeto(self, dicionario):
        return Reserva(**dicionario)

    def cria_elementos(self):
        ListagemBase.cria_elementos(self)

        # define as colunas
        self.tabela['columns'] = ('id_reserva',
                                  'id_ferramenta',
                                  'id_tecnico',
                                  'data_reserva',
                                  'data_entrega',
                                  'status')

        # formata colunas
        self.tabela.column('#0', width=0, stretch=NO)
        self.tabela.column('id_reserva', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('id_ferramenta', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('id_tecnico', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('data_reserva', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('data_entrega', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('status', anchor=CENTER, width=95, stretch=YES)

        # cria cabeçalhos
        self.tabela.heading('id_reserva', text='Id da Reserva', anchor=CENTER)
        self.tabela.heading('id_ferramenta', text='Id da Ferramenta', anchor=CENTER)
        self.tabela.heading('id_tecnico', text='Id do Tecnico', anchor=CENTER)
        self.tabela.heading('data_reserva', text='Data da reserva', anchor=CENTER)
        self.tabela.heading('data_entrega', text='Data da entrega', anchor=CENTER)
        self.tabela.heading('status', text='Status', anchor=CENTER)

        for objeto in self.bd.linhas:
            self.tabela.insert(parent='', index='end',
                               values=(objeto.id_reserva,
                                       objeto.id_ferramenta,
                                       objeto.id_tecnico,
                                       objeto.data_reserva,
                                       objeto.data_entrega,
                                       objeto.status))
            self.linha += 1

        self.tabela.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )
