# Crie um classe chamada cachorro com os atributos:
# nome, raça, idade

class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

ben = Cachorro("Ben", "Shih Tzu", 10)
print(f"Nome: {ben.nome}")
print(f"Raça: {ben.raca}")