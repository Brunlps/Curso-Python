# Crie um classe chamada pessoa com os atributos: nome,
# idade, peso, gênero.

class Pessoa:
    def __init__(self, name: str, age: int, weight: float, gender: str):
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender

    def mostrar_dados_pessoais(self) -> None:
        print(f"""
            Nome: {self.name}
            Idade: {self.age}
            Peso: {self.weight}
            Gênero: {self.gender}""")


pessoa01 = Pessoa("Bruna", 29, 65.3, "Feminino")
pessoa01.mostrar_dados_pessoais()
