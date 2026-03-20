
list_number = []


def dados():
    for element in range(2):
        number = int(input("Digite um número: "))
        list_number.append(number)
        element
    print(list_number)
dados()

def soma():
    calculo = sum(list_number)
    print(calculo)
    
def subtracao():
    calculo = max(list_number) - min(list_number)
    print(calculo)
    
def multiplicar():
    calculo = max(list_number) * min(list_number)
    print(calculo)
    
def divisao():
    calculo = max(list_number) / min(list_number)
    print(calculo)
    
