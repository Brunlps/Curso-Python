# Programa 4.1: lê dois valores e impreime qual é o maior
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
    # Ele vai comparar os valores, se "a" for maior que "b"...
    print('O primeiro valor é maior!')
if b > a:
    # Ele vai comparar os valores, se "b" for maior que "a"...
    print('O segundo valor é maior!')
if a == b:
    print('Os valores são iguais!')
    
# Exercício 4.1: Analise o Programa 4.1. Responda o que aconteca se o 
# Primeiro e o segundo valor foren iguais? Explique.
    """
    Se os valores frorem iguas não acontece nada, porque 
    por as condições só permite verificar valores maiores ou menos. 
    
    Posso criar outro if com o operador de igual( == ),
    
    ou,
    Usar: >=, ou, <=
    Para que o programa verifique se os valores são iguais, tevo adicionar operador relacional
    de igual ( = ).
    
    Dessa forma as condições verificarar se é > ou =, ou, se < ou =.
    """