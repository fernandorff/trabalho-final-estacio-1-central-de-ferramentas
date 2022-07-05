import csv

# Variáveis globais
databasePath = "database.csv"


def main():
    rows = [
        {'nome': 'João', 'sobrenome': 'Da Silva', 'telefone': 123456789, 'turno': 'M', 'equipe': 'B'},
        {'nome': 'Maria', 'sobrenome': 'Dos Santos', 'telefone': 111111111, 'turno': 'M', 'equipe': 'B'},
    ]
    write(rows)
    read()


def write(rows):
    # csv header
    fieldnames = rows[0].keys()

    with open(databasePath, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def read():
    with open(databasePath, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            print(dict(row))


if __name__ == '__main__':
    main()
