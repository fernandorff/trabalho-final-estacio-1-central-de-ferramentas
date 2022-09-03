import tkinter as tk
from models import Ferramenta
from views.janela_base import CadastroBase

class CadastrarFerramenta(CadastroBase):

    def __init__(self):
        CadastroBase.__init__(self, 'Cadastro de Ferramentas', 'ferramentas.csv', altura=450)

        # cria variáveis dos campos:
        self.id_ferramenta = tk.StringVar()
        self.modelo = tk.StringVar()
        self.descricao = tk.StringVar()
        self.fabricante = tk.StringVar()
        self.voltagem = tk.StringVar()
        self.peso_g = tk.StringVar()
        self.tipo = tk.StringVar()
        self.quantidade = tk.StringVar()

        self.cria_elementos()

    def cria_elementos(self):

        opcoes_voltagem = ["110v", "127v", "220v", "380v"]

        opcoes_tipo = ['Camera fotográfica',
                       'Gravador de vídeo',
                       'Gravador de som',
                       'Microfone',
                       'Projetor',
                       'Monitor/Tela',
                       'Placa de vídeo',
                       'Placa de som',
                       'Cabeamento',
                       'Computador',
                       'Iluminação',
                       'Outro'
                       ]

        self.adiciona_campo('Identificação da Ferramenta:', self.id_ferramenta)
        self.adiciona_campo('Modelo:', self.modelo)
        self.adiciona_campo('Descrição:', self.descricao)
        self.adiciona_campo('Fabricante:', self.fabricante)
        self.adiciona_dropdown('Voltagem:', self.voltagem, opcoes_voltagem)
        self.adiciona_campo('Peso em grams:', self.peso_g)
        self.adiciona_dropdown('Tipo:', self.tipo, opcoes_tipo)
        self.adiciona_campo('Quantidade disponivel:', self.quantidade)

        cadastra_button = tk.Button(self.janela, text="Cadastrar", command=self.confirma_cadastro)
        cadastra_button.grid(column=0, row=self.linha + 2, padx=5, pady=8, columnspan=2)

    def cria_objeto(self, dicionario):
        return Ferramenta(**dicionario)

    def confirma_cadastro(self):
        if not self.valida_id():
            return

        # TODO: fazer as outras validações aqui

        ferramenta = Ferramenta(self.id_ferramenta.get(),
                                self.modelo.get(),
                                self.descricao.get(),
                                self.fabricante.get(),
                                self.voltagem.get(),
                                self.peso_g.get(),
                                self.tipo.get(),
                                self.quantidade.get())

        self.salva_cadastro(ferramenta)

    def valida_id(self):
        id_ferramenta = self.id_ferramenta.get()
        if not id_ferramenta.isdigit():
            self.abre_popup('Valor inválido', 'O campo "Id Ferramenta" deve conter apenas números.')
            return False

        return True

    def limpa_campos(self):
        self.id_ferramenta.set('')
        self.modelo.set('')
        self.descricao.set('')
        self.fabricante.set('')
        self.voltagem.set('')
        self.peso_g.set('')
        self.tipo.set('')
        self.quantidade.set('')
