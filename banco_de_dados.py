import csv
import os


class BancoDeDados:
    def __init__(self, caminho, cria_objeto):
        self.caminho = caminho
        self.linhas = []
        self.lê_arquivo(cria_objeto)

    def salvar(self):
        dados = [linha.__dict__ for linha in self.linhas]
        # usa a primeira linha como referência para obter o nome das colunas:
        campos = dados[0].keys()

        # abre o arquivo para escrita:
        with open(self.caminho, 'w', encoding='UTF8', newline='') as f:
            # define a escrita através de dicionários no csv:
            writer = csv.DictWriter(f, fieldnames=campos)
            # escreve as colunas:
            writer.writeheader()
            # escreve as linhas:
            writer.writerows(dados)

    def lê_arquivo(self, cria_objeto):
        # verifica se o arquivo ainda não foi criado:
        if not os.path.exists(self.caminho):
            # caso o arquivo não exista, cria e retorna uma lista vazia:
            with open(self.caminho, 'a', encoding='UTF8') as file:
                return;

        # caso o arquivo já exista, abre ele para leitura:
        with open(self.caminho, 'r', encoding='UTF8') as file:
            csv_file = csv.DictReader(file)
            for linha in csv_file:
                # converte a linha em um dicionário:
                dicionario = dict(linha)
                # passa o dicionário para ser convertido em um objeto:
                objeto = cria_objeto(dicionario)
                self.adiciona_linha(objeto)

    def adiciona_linha(self, objeto):
        self.linhas.append(objeto)
