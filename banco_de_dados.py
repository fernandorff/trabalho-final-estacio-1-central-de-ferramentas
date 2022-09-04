import csv
import os


class BancoDeDados:
    def __init__(self, caminho, cria_objeto):
        self.caminho = caminho
        self.linhas = []
        self.cria_objeto = cria_objeto
        self.le_arquivo()

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

    def le_arquivo(self):
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
                objeto = self.cria_objeto(dicionario)
                self.adiciona_linha(objeto)

    def atualiza(self):
        self.linhas.clear()
        self.le_arquivo()

    def adiciona_linha(self, objeto):
        self.linhas.append(objeto)

    def encontra_linha(self, id_campo, id_valor):
        for linha in self.linhas:
            if linha.__dict__[id_campo] == str(id_valor) or int(linha.__dict__[id_campo]) == id_valor:
                return linha

    def remove_linha(self, id_campo, id_valor):
        linha_à_excluir = self.encontra_linha(id_campo, id_valor)

        if linha_à_excluir is not None:
            self.linhas.remove(linha_à_excluir)

    def altera_linha(self, objeto):
        dicionario = objeto.__dict__
        id_campo = next(iter(dicionario))
        for i, linha in enumerate(self.linhas):
            if linha.__dict__[id_campo] == dicionario[id_campo]:
                self.linhas[i] = objeto
