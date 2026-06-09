"""
    Docstring para Mod02.funcoes.exer03
    [PYIA-A07] Crie uma função chamada lancar_dadosque utilizará o módulo random para 
    simular o lançamento de dois dados. Cada dado deve gerar um número aleatório entre 1 e 6. 
    A função deve somar os resultados desses dois lançamentos e retornar o valor total.
"""
from random import randint


def lancar_dados():

    dados1 = randint(1, 6)
    dados2 = randint(1, 6)

    total = dados1 + dados2

    print(f"Os números escolhidos foram {dados1} e {dados2}")
    return total


result = lancar_dados()

print(f"Total: {result}")
