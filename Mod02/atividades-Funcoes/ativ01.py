# Exercício 8.1:
    # Escreva uma função que retorne o maior de dois números.
    
def numbers(number1, number2):
    if number1 > number2:
        return number1, "É maior"
    else:
        return number2, "É manor"
    
print(numbers(10, 13))

def maior_numero(num1, num2, num3):
    return max(num1, num2, num3)


# Entrada do usuário
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite mais um número: "))

# Processamento dos dados
resultado = maior_numero(n1, n2, n3)

# Saída
print("O maior número é:", resultado)
