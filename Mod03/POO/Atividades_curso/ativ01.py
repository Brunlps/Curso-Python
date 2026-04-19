# Crie um classe chamada cachorro com os atributos:
# nome, raça, idade.
# Classe
class Cachorro:
    # Contrutor de atributos
    def __init__(self, name: str, race: str, age: int):
        self.name = name
        self.race = race
        self.age = age

    def mostr_dados_cachorro(self) -> None:
        print(f"Nome: {self.name} \nRaça: {self.race} \nIdade: {self.age}")


cachorro_01 = Cachorro("Ben", "Shit-zu", 13)
cachorro_01.mostr_dados_cachorro()
