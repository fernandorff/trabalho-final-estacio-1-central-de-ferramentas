from fpdf import FPDF


class Relatorio(FPDF):
    def __init__(self, título):
        FPDF.__init__(self, 'P', 'mm', 'A4')

        self.título = título
        self.title = título
        self.largura_celula = 24
        self.altura_celula = 4
        self.lagura_max = 190
        self.set_draw_color(33, 187, 239)  # azul estácio

    def header(self):
        # Logo
        self.image('estacio_logo.png', 10, 8, 33)
        self.add_font("Arial", "", "arial.ttf", uni=True)
        self.set_font('arial', '', 6.0)
        # Move para a direita
        self.cell(80)
        # Título
        self.cell(50, 10, self.título, 1, 0, 'C')
        # quebra de linha
        self.ln(20)

    def footer(self):
        # Posição a 1.5 cm da parte inferior
        self.set_y(-15)
        self.set_font('Arial', 'I', 5.0)
        # Número das páginas
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def adiciona_colunas(self, colunas: list):
        self.largura_celula = self.lagura_max / len(colunas)

        for coluna in colunas:
            self.adiciona_coluna(coluna)

        self.quebra_linha()

    def adiciona_coluna(self, texto: str):
        self.set_fill_color(34, 172, 191)  # verde estácio
        self.set_text_color(255, 255, 255)  # branco

        texto = self.processa_texto(texto)
        self.cell(self.largura_celula, self.altura_celula, texto, 1, 0, fill=True)

    def adiciona_celula(self, texto: str):
        self.set_text_color(0, 0, 0)  # preto

        texto = self.processa_texto(texto)
        self.cell(self.largura_celula, self.altura_celula, texto, 1, 0, fill=False)

    def processa_texto(self, texto):
        max = 25
        tamanho = len(texto)
        # corta textos muito longos:
        return (texto[:max - 3] + '...') if tamanho > max else texto

    def quebra_linha(self):
        # self.cell(0, self.altura_celula, ln=1)
        self.ln(self.altura_celula)
