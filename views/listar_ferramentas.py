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
                                  'descricao',
                                  'fabricante',
                                  'voltagem',
                                  'peso_g',
                                  'tipo',
                                  'quantidade')

        # formata colunas
        self.tabela.column('#0', width=0, stretch=NO)
        self.tabela.column('id_ferramenta', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('modelo', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('descricao', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('fabricante', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('voltagem', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('peso_g', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('tipo', anchor=CENTER, width=95, stretch=YES)
        self.tabela.column('quantidade', anchor=CENTER, width=95, stretch=YES)

        # cria cabeçalhos
        self.tabela.heading('id_ferramenta', text='Identificaçao da Ferramenta', anchor=CENTER)
        self.tabela.heading('modelo', text='Modelo', anchor=CENTER)
        self.tabela.heading('descricao', text='Descrição', anchor=CENTER)
        self.tabela.heading('fabricante', text='Fabricante', anchor=CENTER)
        self.tabela.heading('voltagem', text='Voltagem', anchor=CENTER)
        self.tabela.heading('peso_g', text='Peso em grams', anchor=CENTER)
        self.tabela.heading('tipo', text='Tipo', anchor=CENTER)
        self.tabela.heading('quantidade', text='Quantidade disponível', anchor=CENTER)

        for objeto in self.bd.linhas:
            self.tabela.insert(parent='', index='end',
                               values=(objeto.id_ferramenta,
                                       objeto.modelo,
                                       objeto.descricao,
                                       objeto.fabricante,
                                       objeto.voltagem,
                                       objeto.peso_g,
                                       objeto.tipo,
                                       objeto.quantidade))
            self.linha += 1

        self.tabela.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )
