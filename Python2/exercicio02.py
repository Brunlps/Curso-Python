"""
    Crie um programa que solicite ao usuário
      o tamanho da base e a altura de um
      triângulo e calcule a sua área.

    area = (base * altura) / 2
"""
base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))
divisor_por2 = 2

area = (base * altura) / divisor_por2

print(f"A área do triângolu é: {area}")
