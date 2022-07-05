import csv

# Variáveis globais
databasePath = "database.csv"


class Tecnico:
    def __init__(self, id_cpf, nome, sobrenome, telefone, turno, equipe):
        self.id_cpf = id_cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.turno = turno
        self.equipe = equipe


def main():
    rows = read()
    menu = 0

    while menu != 9:
        if menu == 1:
            display(rows)
        elif menu == 2:
            tecnico = create_tecnico()
            rows.append(tecnico)
        menu = int(input("\n-Menu Principal----------------------------\n"
                         "Digite 1 para listar técnicos cadastrados.\n"
                         "Digite 2 para cadastrar novo técnico.\n"
                         "Digite 9 para terminar.\n"))

    write(rows)
    read()


def create_tecnico():
    id_cpf = input("Digite o cpf: ")
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    telefone = input("Digite o telefone celular ou rádio: ")
    turno = input("Digite o turno (M = Manhã, T = Tarde, N = Noite): ")
    equipe = input("Digite o nome da equipe: ")
    tecnico = Tecnico(id_cpf, nome, sobrenome, telefone, turno, equipe)
    return tecnico


def write(rows):
    data = [row.__dict__ for row in rows]
    fieldnames = data[0].keys()

    with open(databasePath, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def read():
    rows = []
    with open(databasePath, 'r', encoding='UTF8') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            dicionario = dict(row)
            tecnico = Tecnico(**dicionario)
            rows.append(tecnico)
    return rows


def display(rows):
    for row in rows:
        print(row.__dict__)


if __name__ == '__main__':
    main()
