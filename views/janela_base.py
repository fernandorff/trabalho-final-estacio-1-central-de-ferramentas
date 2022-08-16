import tkinter as tk
from tkinter import *


class JanelaBase(Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        # Inicializa variáveis:
        self.popUp = None

    def define_dimensões(self, janela, largura=800, altura=600):
        # pega as dimensões da tela:
        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()
        # find the center point
        centro_x = int(screen_width / 2 - largura / 2)
        centro_y = int(screen_height / 2 - altura / 2)

        # define a posição da janela para o centro da tela:
        janela.geometry(f'{largura}x{altura}+{centro_x}+{centro_y}')

    def abre_popup(self, titulo, mensagem):
        self.popUp = PopUp(titulo, mensagem)


class PopUp(JanelaBase):
    def __init__(self, título, mensagem):
        JanelaBase.__init__(self)

        self.janela = Toplevel(self)
        self.janela.title(título)
        self.define_dimensões(self.janela, 300, 100)

        label = tk.Label(self.janela, text=mensagem)
        label.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )

        ok_button = tk.Button(
            self.janela,
            text='Ok',
            command=lambda: self.janela.destroy()
        )

        ok_button.pack(
            ipadx=5,
            ipady=5,
            expand=True
        )
