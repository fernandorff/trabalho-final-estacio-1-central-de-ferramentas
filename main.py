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
    rows = [
        Tecnico(12345678901, "João", "Da Silva", 123456789, 'M', 'B'),
        Tecnico(11111111111, "Maria", "Dos Santos", 111111111, 'M', 'B')
    ]
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
