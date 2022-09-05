import tkinter as tk
from models import Ferramenta
from views.cadastro_base import CadastroBase

class CadastrarFerramenta(CadastroBase):

    def __init__(self, janela_criadora=None, ferramenta: Ferramenta = None):
        CadastroBase.__init__(self, 'Cadastro de Ferramentas', 'ferramentas.csv', altura=360)

        self.altera_cadastro = ferramenta
        self.janela_criadora = janela_criadora

        # cria variáveis dos campos:
        self.id_ferramenta = tk.StringVar()
        self.modelo = tk.StringVar()
        self.descricao = tk.StringVar()
        self.fabricante = tk.StringVar()
        self.voltagem = tk.StringVar()
        self.peso_g = tk.StringVar()
        self.tipo = tk.StringVar()
        self.quantidade = tk.StringVar()

        if ferramenta is not None:
            self.id_ferramenta.set(ferramenta.id_ferramenta)
            self.modelo.set(ferramenta.modelo)
            self.descricao.set(ferramenta.descricao)
            self.fabricante.set(ferramenta.fabricante)
            self.voltagem.set(ferramenta.voltagem)
            self.peso_g.set(ferramenta.peso_g)
            self.tipo.set(ferramenta.tipo)
            self.quantidade.set(ferramenta.quantidade)

        self.cria_elementos()

    def cria_elementos(self):

        opcoes_voltagem = ["110v", "127v", "220v", "380v", "Baterias", "N/A"]

        opcoes_tipo = ['Cabeamento',
                       'Caixa de som',
                       'Camera fotográfica',
                       'Computador',
                       'Gravador de som',
                       'Gravador de vídeo',
                       'Iluminação',
                       'Microfone',
                       'Monitor/Tela',
                       'Montagem/Construção',
                       'Placa de som',
                       'Placa de vídeo',
                       'Projetor',
                       'Outros'
                       ]

        self.adiciona_campo('Identificação da Ferramenta:', self.id_ferramenta)
        self.adiciona_campo('Modelo:', self.modelo)
        self.adiciona_campo('Fabricante:', self.fabricante)
        self.adiciona_campo('Descrição:', self.descricao)
        self.adiciona_campo('Peso em grams:', self.peso_g)
        self.adiciona_campo('Quantidade disponivel:', self.quantidade)
        self.adiciona_dropdown('Voltagem:', self.voltagem, opcoes_voltagem)
        self.adiciona_dropdown('Tipo:', self.tipo, opcoes_tipo)

        texto_cadastro = 'Cadastrar' if self.altera_cadastro is None else 'Alterar cadastro'
        cadastra_button = tk.Button(self.janela, text=texto_cadastro, command=self.confirma_cadastro)
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
