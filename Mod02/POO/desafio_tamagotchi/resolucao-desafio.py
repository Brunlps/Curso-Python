# DESAFIO:
# CRIE UMA CLASSE PARA REPRESENTAR UM TAMAGOTCHI
# COM OS ATRIBUTOS: NOME, ESPECIE
# ATRIBUTOS INTERNOS: VIDA_MAX, VIDA_ATUAL, ENERGIA_MAX, ENERGIA_ATUAL, ACORDADO.
# E OS MÉTODOS:
# BRINCAR ( ) - GASTA ENERGIA (20) 
# DORMIR ( ) - REGENERA ENERGIA (50)
# ACORDAR ( ) - APENAS ACORDA.
# LUTAR ( ) - GASTA ENERGIA (30) E GASTA VIDA (25)
# COMER ( ) - REGENERA VIDA (20)
class Tamagotchi:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.vida_max = 100
        self.vida_atual = 100
        self.energia_max = 100
        self.energia_atual = 100
        self.acordado = True

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Vida: {self.vida_atual}/{self.vida_max}")
        print(f"Energia: {self.energia_atual}/{self.energia_max}")
        print(f"Acordado: {'Sim' if self.acordado else 'Não'}")

    def brincar(self):
        if self.acordado and self.energia_atual >= 20:
            self.energia_atual -= 20
            print(f"{self.nome} está brincando! Energia atual: {self.energia_atual}")
        else:
            print(f"{self.nome} não pode brincar agora.")

    def dormir(self):
        if not self.acordado:
            self.energia_atual = min(self.energia_atual + 50, self.energia_max)
            print(f"{self.nome} está dormindo! Energia atual: {self.energia_atual}")
        else:
            print(f"{self.nome} não pode dormir agora.")

    def acordar(self):
        if not self.acordado:
            self.acordado = True
            print(f"{self.nome} acordou!")
        else:
            print(f"{self.nome} já está acordado.")

    def lutar(self):
        if self.acordado and self.energia_atual >= 30 and self.vida_atual >= 25:
            self.energia_atual -= 30
            self.vida_atual -= 25
            print(f"{self.nome} está lutando! Energia atual: {self.energia_atual}, Vida atual: {self.vida_atual}")
        else:
            print(f"{self.nome} não pode lutar agora.")

    def comer(self):
        if self.acordado:
            self.vida_atual = min(self.vida_atual + 20, self.vida_max)
            print(f"{self.nome} está comendo! Vida atual: {self.vida_atual}")
        else:
            print(f"{self.nome} não pode comer agora.")

# Criando um Tamagotchi
tamagotchi1 = Tamagotchi("Tama", "Gato")
# Testando os métodos
while True:
    print("\nEscolha uma ação:")
    print("1. Status")
    print("2. Brincar")
    print("3. Dormir")
    print("4. Acordar")
    print("5. Lutar")
    print("6. Comer")
    print("7. Sair")


    escolha = input("Digite o número da ação: ")
    match escolha:
        case "1": 
            tamagotchi1.status()
        case "2":
            tamagotchi1.brincar()
        case "3":
            tamagotchi1.dormir()
        case "4":
            tamagotchi1.acordar()
        case "5":
            tamagotchi1.lutar()
        case "6":
            tamagotchi1.comer()
        case "7":
            print("Saindo do jogo. Até a próxima!")
            break
        case _:
            print("Opção inválida. Tente novamente.")