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
        self.vida_atual = self.vida_max
        self.energia_max = 200
        self.energia_atual = self.energia_max
        self.acordado = True

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Vida: {self.vida_atual}/{self.vida_max}")
        print(f"Energia: {self.energia_atual}/{self.energia_max}")
        print(f"Acordado: {'Sim' if self.acordado else 'Não'}")

    def brincar(self):
        # BRINCAR ( ) - GASTA ENERGIA (20) 
        if self.acordado and self.energia_atual >= 20:
            self.energia_atual -= 20
            print(f"{self.nome} está brincando!\nEnergia atual: {self.energia_atual}")

        else:
            print(f"{self.nome} não pode brincar agora.")
            
    def dormir(self):
        # DORMIR ( ) - REGENERA ENERGIA (50)
        
        if not self.acordado:
            self.energia_atual = min(self.energia_atual + 50, self.energia_max)
            print(f"{self.nome} está dormindo!\nEnergia atual: {self.energia_atual}")
        else:
            print(f"{self.nome} não pode dormir agora!")
    # ACORDAR() - APENAS ACORDA
    def acordar(self):
        if not self.acordado:
            self.acordado = True
            print(f"{self.nome} acordou!")
        else:
            print(f"{self.nome} já está acordado!")
    def lutar(self):
    # LUTAR ( ) - GASTA ENERGIA (30) E GASTA VIDA (25)
        if self.acordado and self.energia_atual >= 30 and self.energia_atual >= 25:
               self.energia_atual -= 30
               self.vida_atual -= 25
               print(f"{self.nome} esta lutando! \nenergia atual {self.energia_atual} \nVida atual {self.vida_atual}.")

        else:
            print(f"{self.nome} não pode lutar agora.")
    def comer(self):
    # COMER ( ) - REGENERA VIDA (20)
        if self.acordado:
           self.vida_atual = min(self.vida_atual + 20, self.vida_max)
           print(f"{self.nome} está comendo! Vida atual: {self.vida_atual}")
        else:
            print(f"{self.nome} não pode comer agora")
        
        
tamagotchi1 = Tamagotchi("Lulu", "Dragão")

while True:
# BRINCAR ( ) - GASTA ENERGIA (20) 
# DORMIR ( ) - REGENERA ENERGIA (50)
# ACORDAR ( ) - APENAS ACORDA.
# LUTAR ( ) - GASTA ENERGIA (30) E GASTA VIDA (25)
# COMER ( ) - REGENERA VIDA (20)
    
    opcao = int(input("""
            =-=-=-=-=-=Menu=-=-=-=-=-=
                1 - Status
                2 - Brincar
                3 - Dormir
                4 - Acordar
                5 - Lutar
                6 - Comer
                0 - Sair
            =-=-=-=-=-==-=-=-=-=-=
            Escolha um opção: """))
        
        
        
    match opcao:
        case 1:
            tamagotchi1.status()
        case 2:
            tamagotchi1.brincar()
        case 3:
            tamagotchi1.dormir()
        case 4:
            tamagotchi1.acordar()
        case 5:
            tamagotchi1.lutar()
        case 6:
            tamagotchi1.comer()
        case 0:
            print("Saindo...")
            break
        case _:
            print("Entrada inválida!")
