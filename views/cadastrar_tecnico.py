import tkinter as tk
from models import Tecnico
from views.janela_base import CadastroBase


class CadastrarTécnico(CadastroBase):
    def __init__(self):
        CadastroBase.__init__(self, 'Cadastro de Técnicos', 'tecnicos.csv')

        # cria variáveis dos campos:
        self.cpf = tk.StringVar()
        self.nome = tk.StringVar()
        self.sobrenome = tk.StringVar()
        self.telefone = tk.StringVar()
        self.equipe = tk.StringVar()
        self.turno = tk.StringVar()

        self.cria_elementos()

    def cria_elementos(self):
        self.adiciona_campo('CPF:', self.cpf)
        self.adiciona_campo('Nome:', self.nome)
        self.adiciona_campo('Sobrenome:', self.sobrenome)
        self.adiciona_campo('Telefone:', self.telefone)
        self.adiciona_campo('Turno:', self.turno)
        self.adiciona_campo('Equipe:', self.equipe)

        cadastra_button = tk.Button(self.janela, text="Cadastrar", command=self.cadastra_técnico)
        cadastra_button.grid(column=0, row=self.linha + 2, padx=5, pady=8, columnspan=2)

    def cria_objeto(self, dicionario):
        return Tecnico(**dicionario)

    def cadastra_técnico(self):
        # validações
        if not self.valida_cpf():
            return

        # TODO: fazer as outras validações aqui

        tecnico = Tecnico(self.cpf.get(),
                          self.nome.get(),
                          self.sobrenome.get(),
                          self.telefone.get(),
                          self.turno.get(),
                          self.equipe.get())

        self.salva_cadastro(tecnico)

    def valida_cpf(self):
        cpf = self.cpf.get()
        if not cpf.isdigit():
            self.abre_popup('Valor inválido', 'O campo CPF deve conter apenas números.')
            return False

        if len(cpf) != 11:
            self.abre_popup('Valor inválido', 'O campo CPF deve conter 11 dígitos')
            return False

        return True

    def limpa_campos(self):
        self.cpf.set('')
        self.nome.set('')
        self.sobrenome.set('')
        self.telefone.set('')
        self.turno.set('')
        self.equipe.set('')