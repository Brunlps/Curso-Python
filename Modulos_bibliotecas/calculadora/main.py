# ATIVIDADE PRÁTICA 1

# Crie um programa que será uma calculadora.

# Nesta calculadora você deverá ter um módulo para as
# operações matemáticas, o arquivo principal deverá
# conter apenas um menu de escolha para o usuário

# (soma, subtração, multiplicação e divisão).
from calculadora import *

while True:
    
    opcao = int(input("""
            =-=-=-=-=-=Menu=-=-=-=-=-=
                1 - Somar
                2 - Subtração
                3 - Multiplicação
                4 - Divisão
                5 - Sair
            =-=-=-=-=-==-=-=-=-=-=
            Escolha um opção: """))
    if opcao <= 0:
        print("Opção inválida, digite numeros de 1 a 5.")
        
    else:
        
        match opcao:
            case 1:
                soma()
            case 2:
                subtracao()
            case 3:
                multiplicar()
            case 4:
                divisao()
            case 5:
                print("Saindo...")
                break