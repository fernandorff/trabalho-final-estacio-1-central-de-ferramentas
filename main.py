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
    rows = []
    menu = 1

    while menu != 9:
        id_cpf = input("Digite o cpf: ")
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        telefone = input("Digite o telefone celular ou rádio: ")
        turno = input("Digite o turno (M = Manhã, T = Tarde, N = Noite): ")
        equipe = input("Digite o nome da equipe: ")
        rows.append(Tecnico(id_cpf, nome, sobrenome, telefone, turno, equipe))
        menu = int(input("Para adicionar novo Técnico, digite 1, para terminar, digite 9: "))

    write(rows)
    read()


def write(rows):
    data = [row.__dict__ for row in rows]
    fieldnames = data[0].keys()

    with open(databasePath, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def read():
    with open(databasePath, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            print(dict(row))


if __name__ == '__main__':
    main()
