"""
[PYIA-A07] Crie uma função chamada lancar_dados que utilizará o módulo random
para simular o lançamento de dois dados. Cada dado deve gerar um número aleatório
entre 1 e 6. A função deve somar os resultados desses dois lançamentos e retornar o valor total.
"""
import random

def lancar_dados():
    dados1 = [1, 2, 3, 4, 5, 6]
    dados2 = [1, 2, 3, 4, 5, 6]

    for numero_escolhido in random(dados1):