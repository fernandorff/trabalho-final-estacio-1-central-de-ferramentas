import tkinter as tk
from models import Ferramenta
from views.janela_base import CadastroBase


class CadastrarFerramenta(CadastroBase):
    def __init__(self):
        CadastroBase.__init__(self, 'Cadastro de Ferramentas', 'ferramentas.csv', altura=450)

        # cria variáveis dos campos:
        self.id_ferramenta = tk.StringVar()
        self.modelo = tk.StringVar()
        self.descrição = tk.StringVar()
        self.fabricante = tk.StringVar()
        self.voltagem = tk.StringVar()
        self.part_num = tk.StringVar()
        self.tamanho = tk.StringVar()
        self.unidade_tamanho = tk.StringVar()
        self.tipo = tk.StringVar()
        self.material = tk.StringVar()
        self.reserva_máxima = tk.StringVar()

        self.cria_elementos()

    def cria_elementos(self):
        self.adiciona_campo('Identificação da Ferramenta', self.id_ferramenta)
        self.adiciona_campo('Modelo', self.modelo)
        self.adiciona_campo('Descrição', self.descrição)
        self.adiciona_campo('Fabricante', self.fabricante)
        self.adiciona_campo('Voltagem', self.voltagem)
        self.adiciona_campo('Part Number', self.part_num)
        self.adiciona_campo('Tamanho', self.tamanho)
        self.adiciona_campo('Unidade de medida', self.unidade_tamanho)
        self.adiciona_campo('Tipo', self.tipo)
        self.adiciona_campo('Material', self.material)
        self.adiciona_campo('Tempo máximo de reserva', self.reserva_máxima)

        cadastra_button = tk.Button(self.janela, text="Cadastrar", command=self.confirma_cadastro)
        cadastra_button.grid(column=0, row=self.linha + 2, padx=5, pady=8, columnspan=2)

    def cria_objeto(self, dicionario):
        return Ferramenta(**dicionario)

    def confirma_cadastro(self):
        ferramenta = Ferramenta(self.id_ferramenta.get(),
                                self.modelo.get(),
                                self.descrição.get(),
                                self.fabricante.get(),
                                self.voltagem.get(),
                                self.part_num.get(),
                                self.tamanho.get(),
                                self.unidade_tamanho.get(),
                                self.tipo.get(),
                                self.material.get(),
                                self.reserva_máxima.get())

        # TODO: realizar validações dos campos
        self.salva_cadastro(ferramenta)

    def limpa_campos(self):
        self.id_ferramenta.set('')
        self.modelo.set('')
        self.descrição.set('')
        self.fabricante.set('')
        self.voltagem.set('')
        self.part_num.set('')
        self.tamanho.set('')
        self.unidade_tamanho.set('')
        self.tipo.set('')
        self.material.set('')
        self.reserva_máxima.set('')
