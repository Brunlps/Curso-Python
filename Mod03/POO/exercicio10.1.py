class Televisao:
    def __init__(self, canal_min=3, canal_max=10, canal=10):
        self.ligada = True
        self.canal = canal
        self.tamanho = 40
        self.modelo = "Samsung"
        # Foi adicionado os atributos de 
        # canal_min e canal_max para limitar os 
        # canais que a televisão pode acessar
        self.canal_min = canal_min 
        self.canal_max = canal_max
        
    # Adicionando os métodos para mudar para baixo,
    # verificando se o canal atual é maior ou igual ao canal mínimo.
    def mudar_canal_para_baixo(self):
        
        if self.canal - 1 >= self.canal_min:
            self.canal -= 1
            
    # Adicionamos o método para mudar o canal para cima, 
    # verificando se o canal atual é menor ou igual ao canal máximo.
    def mudar_canal_para_cima(self):

        if self.canal + 1 <= self.canal_max:
            self.canal += 1

tv_quarto = Televisao()

print(f"TV esta esta ligada: {tv_quarto.ligada}")

# O canal inicial é 2, e o canal máximo é 13. 
# Então, ao tentar mudar o canal para cima 12 vezes, 
# ele deve parar no canal 13.

for i in range(0, 12):
    tv_quarto.mudar_canal_para_cima()
print(f"Mudar canal para cima: {tv_quarto.canal}")  

# O canal atual é 13, e o canal mínimo é 2.
# Então, ao tentar mudar o canal para baixo 12 vezes,
# ele deve parar no canal 2.
for i in range(0, 12):
    tv_quarto.mudar_canal_para_baixo()
print(f"Mudar canal para baixo: {tv_quarto.canal}")

# print(f"Tamanho: {tv_quarto.tamanho}")
# print(f"Modelo: {tv_quarto.modelo}")
print("--------------------------------------------------")
# Televisão sala
tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal_min = "jornal"
tv_sala.canal_max = "desenho"
tv_sala.tamanho = 50
tv_sala.modelo = "LG"
print(f"TV esta esta ligada: {tv_sala.ligada}")
print(f"Canal: {tv_sala.canal}")
print(f"Tamanho: {tv_sala.tamanho}")
print(f"Modelo: {tv_sala.modelo}")

