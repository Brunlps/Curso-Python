# Crie um classe chamada pessoa com os atributos: 
# nome, idade, peso, gênero

class Pessoa:
    def __init__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero
        

pessoa1 = Pessoa("Bruna", 30, 65, "Feminino")
print(f"Nome: {pessoa1.nome}")
print(f"Idade: {pessoa1.idade}")
        