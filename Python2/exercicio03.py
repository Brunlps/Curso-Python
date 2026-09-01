"""
Crie um programa que solicite
 a massa e a altura do usuário e calcule seu IMC.

 imc = peso / (altura * altura)
"""
peso_usuario = float(input("Digite o seu peso: "))
altura_usuario = float(input("Digite o seu altura: "))

imc_usuario = peso_usuario / (altura_usuario * altura_usuario)

print(f"O IMC do usuário é: {imc_usuario}")