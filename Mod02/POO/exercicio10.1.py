class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 40
        self.modelo = "Samsung"

tv_quarto = Televisao()
print(f"TV esta esta ligada: {tv_quarto.ligada}")
print(f"Cana: {tv_quarto.canal}")
print(f"Tamanho: {tv_quarto.tamanho}")
print(f"Modelo: {tv_quarto.modelo}")

# Televisão sala
tv_sala = Televisao()
tv_sala.ligada = True
tv_sala.canal = 4
tv_sala.tamanho = 50
tv_sala.modelo = "LG"
print(f"TV esta esta ligada: {tv_sala.ligada}")
print(f"Canal: {tv_sala.canal}")
print(f"Tamanho: {tv_sala.tamanho}")
print(f"Modelo: {tv_sala.modelo}")
