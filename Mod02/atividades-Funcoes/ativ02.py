# Exercício 8.2:
    # Escreva uma função que receba dois números 
    # e retorne True se o primeiro número for multiplo do segundo.
    
number1 = int(input("Digite uma número: "))
number2 = int(input("Digite outro número: "))

def numbers_multiplos(number1, number2):
    if number1 % number2 == 0:
        return True
    else:
        return False
    


print(numbers_multiplos(number1, number2))