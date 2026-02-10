# Exercício 8.1:
    # Escreva uma função que retorne o maior de dois números.
    
def numbers(number1, number2):
    if number1 > number2:
        return number1, "É maior"
    else:
        return number2, "É manor"
    
print(numbers(10, 13))