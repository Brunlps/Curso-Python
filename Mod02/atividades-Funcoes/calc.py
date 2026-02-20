'''
Docstring for Mod02.atividades-Funcoes.calc
    Aqui aconteceram três coisas:
    
    1. numero1 foi repetido.
    
    2. numero2 nem apareceu.
    
    3. Você não precisava declarar numero1 e numero2 como global porque só estava lendo eles, não modificando.
'''
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

result = 0 # Variável global


# Calculadora criada usando funções variável global
def soma():
    global result
    result = numero1 + numero2
def subtracao():
    global result
    result = numero1 - numero2
    
def divisao():
    global result
    result = numero1 / numero2
    
def multiplicacao():
    global result
    result = numero1 * numero2


soma()
print(result)
subtracao()
print(result)
divisao()
print(result)
multiplicacao()
print(result)

