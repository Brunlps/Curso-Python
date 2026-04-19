# Crie um classe chamada cachorro com os atributos:
# nome, raça, idade
class Animal:
    def __init__(self, nome: str, raca: str, cor: str, idade: int):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.idade = idade

    def comer(self) -> None:
        print(f"O {self.nome} comeu!")

    def dormir(self) -> None:
        print(f"O {self.nome} Dormiu!")

    def acordar(self) -> None:
        print(f"O {self.nome} acordou!")

    def emitir_som(self) -> None:
        print(f"O {self.nome} esta latindo!")


class Cachorro(Animal):
    def __init__(self, nome, raca, cor, idade):
        super().__init__(nome, raca, cor, idade)

    def emitir_som(self) -> None:
        print("Faz auau!")
    
    def pega_bolinha(self) -> None:
        print(f"O {self.nome} pegou a bolinha!")


ben = Cachorro("Ben", "Shih Tzu", "Preto", 10, "Puro")
ben.comer()
ben.dormir()
ben.acordar()
ben.emitir_som()
ben.pega_bolinha()


class Gato(Animal):
    def __init__(self, nome, raca, cor, idade):
        super().__init__(nome, raca, cor, idade)

    def miar(self) -> None:
        print(f"O {self.nome} esta miando!")

    def amassar_paozinho(self) -> None:
        print("O {self.nome} esta fazendo carrinho!")


# cat = Gato("Mimi", "Tigre", "Amarelo", 12, "Azul")
# cat.comer()
# cat.domir()
# cat.acordar()
# cat.miar()
# cat.amassar_paozinho()


# class Passaro:
#     def __init__(self, nome: str, raca: str, cor: str, idade: int):
#         self.nome = nome
#         self.raca = raca
#         self.cor = cor
#         self.idade = idade

#     def comer(self) -> None:
#         print(f"O {self.nome} comeu!")

#     def dormir(self) -> None:
#         print(f"O {self.nome} comeu!")

#     def acordar(self) -> None:
#         print(f"O {self.nome} comeu!")

#     def cantar(self) -> None:
#         print(f"O {self.nome} comeu!")


# passaro1 = Passaro("Lulu", "Pombo", "Branco", 2)
# print(passaro1.comer())
# print(passaro1.domir())
# print(passaro1.acordar())
# print(passaro1.cantar())
