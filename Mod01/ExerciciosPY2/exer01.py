"""
    1) Faça um programa que pede a idade de uma 
    pessoa e diga se ela é maior ou menor de idade. 
"""
idade = int(input("Digite a sua idade: "))
if idade <= 0:
    print("Valor inválido!")
elif idade > 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

