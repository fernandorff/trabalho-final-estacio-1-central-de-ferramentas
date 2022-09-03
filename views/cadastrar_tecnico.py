import tkinter as tk
from models import Tecnico
from views.janela_base import CadastroBase

class CadastrarTécnico(CadastroBase):

    def __init__(self):
        CadastroBase.__init__(self, 'Cadastro de Técnicos', 'tecnicos.csv', 500, 350)

        # cria variáveis dos campos:
        self.cpf = tk.StringVar()
        self.nome = tk.StringVar()
        self.sobrenome = tk.StringVar()
        self.telefone = tk.StringVar()
        self.equipe = tk.StringVar()
        self.turno = tk.StringVar()

        self.cria_elementos()

    def cria_elementos(self):
        self.adiciona_campo('CPF:\n (11 digitos, apenas numeros)', self.cpf)
        self.adiciona_campo('Nome:', self.nome)
        self.adiciona_campo('Sobrenome:', self.sobrenome)
        self.adiciona_campo('Telefone com DDD:\n (11 digitos, sem parenteses)', self.telefone)
        self.adiciona_campo('Turno:\n (M=Manhã, T=Tarde, N=Noite)', self.turno)
        self.adiciona_campo('Equipe:\n (Apenas a letra da equipe)', self.equipe)

        cadastra_button = tk.Button(self.janela, text="Cadastrar", command=self.cadastra_técnico)
        cadastra_button.grid(column=0, row=self.linha + 2, padx=5, pady=8, columnspan=2)

    def cria_objeto(self, dicionario):
        return Tecnico(**dicionario)

    def cadastra_técnico(self):
        # validações
        if not self.valida_cpf():
            return
        if not self.valida_nome():
            return
        if not self.valida_sobrenome():
            return
        if not self.valida_telefone():
            return
        if not self.valida_turno():
            return
        if not self.valida_equipe():
            return

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

    def valida_nome(self):
        nome = self.nome.get()

        if not nome.isalpha():
            self.abre_popup('Nome invalido', 'O campo Nome deve conter apenas letras.')
            return False

        if len(nome) < 3:
            self.abre_popup('Valor inválido', 'O campo nome deve conter pelo menos 3 letras')
            return False

        return True

    def valida_sobrenome(self):
        sobrenome_list = self.sobrenome.get().split(' ')
        sobrenome = ''.join(sobrenome_list)

        if not sobrenome.isalpha():
            self.abre_popup('Sobrenome invalido', 'O campo Sobrenome deve conter apenas letras e espaço.')
            return False

        if len(sobrenome) < 3:
            self.abre_popup('Valor inválido', 'O campo Sobrenome deve conter pelo menos 3 caracteres')
            return False

        return True

    def valida_telefone(self):
        telefone = self.telefone.get()
        if not telefone.isdigit():
            self.abre_popup('Valor inválido', 'O campo Telefone deve conter apenas números.')
            return False

        if len(telefone) != 11:
            self.abre_popup('Valor inválido', 'O campo Telefone deve conter 11 dígitos')
            return False

        return True

    def valida_turno(self):
        turno = self.turno.get()
        turnos_validos = ['M', 'T', 'N']
        if turno not in turnos_validos:
            self.abre_popup('Turno invalido', 'O campo Turno deve conter apenas M, T ou N.')
            return False

        return True

    def valida_equipe(self):
        equipe = self.equipe.get()

        if not equipe.isupper():
            self.abre_popup('Equipe invalida', 'O campo Equipe deve conter apenas uma letra maiuscula.')
            return False

        return True

    def limpa_campos(self):
        self.cpf.set('')
        self.nome.set('')
        self.sobrenome.set('')
        self.telefone.set('')
        self.turno.set('')
        self.equipe.set('')
