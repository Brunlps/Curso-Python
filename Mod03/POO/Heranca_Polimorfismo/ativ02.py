#Classe principal
class Mamifaro:
    def __init__(self, localizacao: str):
        self.localizao = localizacao

    def andar(self) -> None:  # Não retorna nada
        print(f"O animal esta andando pelo {self.localizao}")


# Subclasses
class Cachorro(Mamifaro):
    def __init__(self, localizacao):
        super().__init__(localizacao)

    def latir(self) -> None:
        print(f"O Ben esta latindo na {self.localizao}")


class Gato(Mamifaro):
    def __init__(self, localizacao):
        super().__init__(localizacao)

    def miar(self) -> None:
        print(f"O Jubileu esta miando na {self.localizao}")


animal = Mamifaro("Brasil")
animal.andar()

ben = Cachorro("Espanha")
ben.latir()

arodo = Gato("Holanda")
arodo.miar()