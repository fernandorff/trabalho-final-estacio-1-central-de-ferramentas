import tkinter as tk
from tkinter import Frame
from PIL import Image, ImageTk
from views.janela_base import JanelaBase
from views.menu_principal import MenuPrincipal


class LoginAdmin(JanelaBase):
    def __init__(self):
        JanelaBase.__init__(self)

        # Título da janela:
        self.master.title('Login')
        self.master['bg'] = '#BFE0D6'

        # Ajusta tamanho e posição da tela:
        self.define_dimensões(self.master)

        # Inicializa variáveis:
        self.janela = None
        self.linha_topo = 0
        self.linha_login = 0
        self.email = tk.StringVar()
        self.senha = tk.StringVar()

        self.topo = Frame(self.master)
        self.login = Frame(self.master)
        self.rodapé = Frame(self.master)

        # logo:
        logo_arquivo = Image.open("estacio_logo.png")
        logo = ImageTk.PhotoImage(logo_arquivo)

        label = tk.Label(self.topo, image=logo, anchor=tk.CENTER)
        label.image = logo
        # label.pack()
        label.grid(column=0, row=self.linha_login, columnspan=2, sticky=tk.EW)
        self.linha_topo += 1

        # título:
        label = tk.Label(self.topo, text='Trabalho de Certificação Mundo 1 - Grupo 7', font=('Helvetica bold', 18))
        label.config(bg='#21BBEF')
        label.grid(column=0, row=self.linha_topo, sticky=tk.EW, padx=10, pady=10)

        self.linha_topo += 1

        # grupo:
        label = tk.Label(self.topo, text='Membros da equipe', font=('Helvetica bold', 14))
        label.config(bg='#BFE0D6')
        label.grid(column=0, row=self.linha_topo, sticky=tk.EW)
        self.linha_topo += 1

        # membros:
        membros = ['Alessandro Thury de Oliveira',
                   'Fernando Rocha Fonteles Filho',
                   'Gilson Miranda Neto',
                   'Julio Cesar Navagantes Gouveia',
                   'Mariana Lucas Fernandes Onorio'
                   ]
        for membro in membros:
            label = tk.Label(self.topo, text=membro, font=('Helvetica bold', 12))
            label.grid(column=0, row=self.linha_topo, sticky=tk.EW)
            label.config(bg='#BFE0D6')
            self.linha_topo += 1

        # login:
        label = tk.Label(self.login, text='Autenticação', font=('Helvetica bold', 14))
        label.grid(column=0, row=self.linha_login, columnspan=2, sticky=tk.W)
        self.linha_login += 1

        # campo email:
        label = tk.Label(self.login, text='Email')
        label.grid(column=0, row=self.linha_login, sticky=tk.W, padx=5, pady=8)

        entry = tk.Entry(self.login, textvariable=self.email)
        entry.grid(column=1, row=self.linha_login, sticky=tk.EW, padx=10, pady=5)

        self.linha_login += 1

        # campo senha:
        label = tk.Label(self.login, text='Senha')
        label.grid(column=0, row=self.linha_login, sticky=tk.W, padx=5, pady=8)

        entry = tk.Entry(self.login, textvariable=self.senha, show='*', width=16)
        entry.grid(column=1, row=self.linha_login, sticky=tk.EW, padx=10, pady=5)

        self.linha_login += 1

        # botão login:
        login_button = tk.Button(self.login, text='Entrar',
                                 command=self.abre_menu,
                                 relief='solid',
                                 bg='#21BBEF',
                                 fg='white',
                                 highlightcolor="#37d3ff",
                                 borderwidth=1,
                                 font=15)

        login_button.grid(column=0, row=self.linha_login, columnspan=2, sticky=tk.EW, padx=10, pady=10, ipadx=10,
                          ipady=10)

        self.topo.pack(
            pady=10,
            expand=True
        )

        self.login.pack(
            expand=True
        )

        self.rodapé.pack(
            expand=True,
            pady=70
        )

    def abre_menu(self):
        if self.email.get() == '' and self.senha.get() == '':
            self.login.pack_forget()
            self.rodapé.pack_forget()
            self.janela = MenuPrincipal()
        else:
            self.abre_popup('Credenciais inválidas', 'Seu email ou usuário estão incorretos.')
