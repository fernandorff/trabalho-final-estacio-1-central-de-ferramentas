from tkinter import *
from models import Tecnico
from views.cadastrar_tecnico import CadastrarTécnico
from views.listagem_base import ListagemBase


class ListarTécnicos(ListagemBase):
    def __init__(self):
        ListagemBase.__init__(self, 'Listagem de Técnicos', 'tecnicos')

    def cria_objeto(self, dicionario):
        return Tecnico(**dicionario)

    def popula_tabela(self):
        # define as colunas
        self.tabela['columns'] = ('id_cpf',
                                  'nome',
                                  'sobrenome',
                                  'telefone',
                                  'turno',
                                  'equipe')

        # formata colunas
        self.tabela.column('#0', width=0, stretch=NO)
        self.tabela.column('id_cpf', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('nome', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('sobrenome', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('telefone', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('turno', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('equipe', anchor=CENTER, width=95, stretch=YES)

        # cria cabeçalho
        self.tabela.heading('id_cpf', text='Cpf', anchor=CENTER)
        self.tabela.heading('nome', text='Nome', anchor=CENTER)
        self.tabela.heading('sobrenome', text='Sobrenome', anchor=CENTER)
        self.tabela.heading('telefone', text='Telefone', anchor=CENTER)
        self.tabela.heading('turno', text='Turno', anchor=CENTER)
        self.tabela.heading('equipe', text='Equipe', anchor=CENTER)

        for objeto in self.bd.linhas:
            self.tabela.insert(parent='', index='end',
                               values=(objeto.id_cpf,
                                       objeto.nome,
                                       objeto.sobrenome,
                                       objeto.telefone,
                                       objeto.turno,
                                       objeto.equipe))

        self.tabela.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )

    def abre_alterar_cadastro(self, tecnico: Tecnico):
        self.janela_altera_cadastro = CadastrarTécnico(self, tecnico)
