# Criando tuplas

lista_frutas = ("Maça", "Banana", "Laranja", "Abacaxi")

print("==================== Método Índice() ===============================")
#Método index(): Retorna o índice do primeiro
# elemento específicado
indice_laranja = lista_frutas.index("Laranja")
print(f"Índice da laranja: {indice_laranja}")

indice_maca = lista_frutas.index("Maça")
print(f"Índice de maça: {indice_maca}")
# ===================================================
print("==================== Método Cout() ===============================")

# Métodos count():
# Retorna o número de ocorrências de um elemento
quantidade_bananas = lista_frutas.count("Banana")
print(f"Quantidade de bananas: {quantidade_bananas}")