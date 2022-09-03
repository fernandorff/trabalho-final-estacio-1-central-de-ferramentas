from tkinter import *
from models import Ferramenta
from views.janela_base import ListagemBase


class ListarFerramentas(ListagemBase):
    def __init__(self):
        ListagemBase.__init__(self, 'Listagem de Ferramentas', 'ferramentas.csv')

        self.cria_elementos()

    def cria_objeto(self, dicionario):
        return Ferramenta(**dicionario)

    def cria_elementos(self):
        ListagemBase.cria_elementos(self)

        # define as colunas
        self.tabela['columns'] = ('id_ferramenta',
                                  'modelo',
                                  'descrição',
                                  'fabricante',
                                  'voltagem',
                                  'part_num',
                                  'tamanho',
                                  'unidade_tamanho',
                                  'tipo',
                                  'material',
                                  'reserva_máxima')

        # formata colunas
        self.tabela.column('#0', width=0, stretch=NO)
        self.tabela.column('id_ferramenta', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('modelo', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('descrição', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('fabricante', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('voltagem', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('part_num', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('tamanho', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('unidade_tamanho', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('tipo', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('material', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('reserva_máxima', anchor=CENTER, width=95, stretch=YES)

        # cria cabeçalhos
        self.tabela.heading('id_ferramenta', text='Identificaçao da Ferramenta', anchor=CENTER)
        self.tabela.heading('modelo', text='Modelo', anchor=CENTER)
        self.tabela.heading('descrição', text='Descrição', anchor=CENTER)
        self.tabela.heading('fabricante', text='Fabricante', anchor=CENTER)
        self.tabela.heading('voltagem', text='Voltagem', anchor=CENTER)
        self.tabela.heading('part_num', text='Part Number', anchor=CENTER)
        self.tabela.heading('tamanho', text='Tamanho', anchor=CENTER)
        self.tabela.heading('unidade_tamanho', text='Unidade de medida', anchor=CENTER)
        self.tabela.heading('tipo', text='Tipo', anchor=CENTER)
        self.tabela.heading('material', text='Material', anchor=CENTER)
        self.tabela.heading('reserva_máxima', text='Tempo máximo de reserva', anchor=CENTER)

        for objeto in self.bd.linhas:
            self.tabela.insert(parent='', index='end',
                               values=(objeto.id_ferramenta,
                                       objeto.modelo,
                                       objeto.descrição,
                                       objeto.fabricante,
                                       objeto.voltagem,
                                       objeto.part_num,
                                       objeto.tamanho,
                                       objeto.unidade_tamanho,
                                       objeto.tipo,
                                       objeto.material,
                                       objeto.reserva_máxima))
            self.linha += 1

        self.tabela.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )
