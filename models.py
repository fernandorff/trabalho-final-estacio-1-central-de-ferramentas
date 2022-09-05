class Tecnico:

    def __init__(self, id_cpf, nome, sobrenome, telefone, turno, equipe):
        self.id_cpf = id_cpf
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()
        self.telefone = telefone
        self.turno = turno
        self.equipe = equipe

class Ferramenta:

    def __init__(self, id_ferramenta, modelo, descricao, fabricante, voltagem, peso_g, tipo, quantidade):
        self.id_ferramenta = id_ferramenta
        self.modelo = modelo
        self.descricao = descricao
        self.fabricante = fabricante
        self.voltagem = voltagem
        self.peso_g = peso_g
        self.tipo = tipo
        self.quantidade = quantidade

class Reserva:

    def __init__(self, id_reserva, id_ferramenta, id_tecnico, data_reserva, data_entrega, status):
        self.id_reserva = id_reserva
        self.id_ferramenta = id_ferramenta
        self.id_tecnico = id_tecnico
        self.data_reserva = data_reserva
        self.data_entrega = data_entrega
        self.status = status
