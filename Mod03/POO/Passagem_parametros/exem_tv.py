class Televisao:
    # Passando parâmetros
    def __init__(self, canal_min, canal_max):
        self.ligada = False
        self.canal = 2
        self.canal_min = canal_min
        self.canal_max = canal_max

    # Métodos para mudar o canal
    def mudar_canal_baixo(self):
        # uma condição para diminuir o canal
        # sem que ele chegue em número menores que o inicado
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1

    def mudar_canal_cima(self):
        # condicional para aumentar o valor do canal
        # em que ele ultrapasse o número máximo de canais
        if self.canal + 1 <= self.canal_max:
            self.canal += 1


tv = Televisao(1, 99)

# Um loop para diminuir os canais
for x in range(0, 120):
    tv.mudar_canal_cima()

print(tv.canal)

# Um loop para diminuir os canais
for x in range(0, 120):
    tv.mudar_canal_baixo()
print(tv.canal)
