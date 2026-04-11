class Animal:
    # def __init__(self, nome):
    #     self.nome = nome

    # método da classe
    def fazer_som(self):
        pass


class Gato(Animal):
    def fazer_som(self):
        # self.nome = "lula"
        return "Meoow!"


class Cachorro(Animal):
    def fazer_som(self):
        # self.nome = "Rex"
        return "Woof!"


# criando uma nova função para fazer os animais falarem
def fazer_animal_falar(animal):
    return animal.fazer_som()


# objetos sendo instaciados da subclasse
lula = Gato()
rex = Cachorro()

# criando uma lista com objetos
animais = [lula, rex]

# criando um para os animais com as suas falas
for animal in animais:
    print(animal.__class__.__name__, "faz", fazer_animal_falar(animal))
