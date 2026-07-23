# Criando lista com números aleatórios.

lista_numeros_aleatorios = [3, 2, 4, 45, 87, 96, 64, 77, 99, 33, 73, 67, 22]

# Criar um for para somar todos números pares

soma_pares = 0

for numeros in lista_numeros_aleatorios:

    if numeros % 2 == 0:

        soma_pares += numeros

# Imprimir a somar deles.
print(soma_pares)
