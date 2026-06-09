"""
[PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos.
Esta função deve comparar os três números e identificar qual deles é o maior. Para isso,
utilize uma estrutura de controle que verifique qual
número é maior que os outros dois. A função deve então retornar o maior número encontrado.
"""

# primeiro_numero = 0
# segundo_numero = 0
# terceiro_numero = 80


def maior_numero(primeiro_numero, segundo_numero, terceiro_numero) -> None:

    maior_numero_encontrado = 0

    if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
        maior_numero_encontrado = primeiro_numero

    elif segundo_numero > terceiro_numero:
        maior_numero_encontrado = segundo_numero

    else:
        maior_numero_encontrado = terceiro_numero

    print(f"o maios número é: {maior_numero_encontrado}")


maior_numero(630, 30, 45)
