class Tecnico:
    def __init__(self, id_cpf, nome, sobrenome, telefone, turno, equipe):
        self.id_cpf = id_cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.turno = turno
        self.equipe = equipe


class Ferramenta:
    def __init__(self, id_ferramenta, modelo, descrição, fabricante, voltagem, part_num, tamanho, unidade_tamanho, tipo,
                 material, reserva_máxima):
        self.id_ferramenta = id_ferramenta
        self.modelo = modelo
        self.descrição = descrição
        self.fabricante = fabricante
        self.voltagem = voltagem
        self.part_num = part_num
        self.tamanho = tamanho
        self.unidade_tamanho = unidade_tamanho
        self.tipo = tipo
        self.material = material
        self.reserva_máxima = reserva_máxima
