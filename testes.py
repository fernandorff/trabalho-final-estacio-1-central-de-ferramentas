# importing the module
import csv

filename = open('tecnicos.csv', 'r')

file = csv.DictReader(filename)

id_cpf = []
nome = []
sobrenome = []

for col in file:
    id_cpf.append(col['id_cpf'])
    nome.append(col['nome'])
    sobrenome.append(col['sobrenome'])

opcoes_tecnico = []

index = 0
for i in id_cpf:
    conjunto = [id_cpf[index], nome[index], sobrenome[index]]
    opcoes_tecnico.append(' '.join(conjunto))
    index += 1

print(opcoes_tecnico)