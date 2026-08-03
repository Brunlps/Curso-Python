numeros = [0, 0, 0, 0, 0]

x = 0

while x < 5:
    numeros[x] = int(input(f"Números {x + 1}: "))
    x += 1

while True:
    escolhido = int(input("Que posicão você quer imprimir (0 para Sair)"))

    if escolhido == 0:
        break
    print(f"Você escolheu o números: {numeros[escolhido - 1]}")
