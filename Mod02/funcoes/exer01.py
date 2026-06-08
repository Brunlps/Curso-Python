
# PYIA-A04] Crie uma função chamada media que
# receba três números como argumentos. Esta função
# deve calcular a média aritmética desses três números.
# Para fazer isso, alguns dos três números e, em seguida,
# divide o resultado por três. Por fim,
# a função deve retornar o valor da média aritmética calculada.

def mediaTresNumeros(primeiro_numero, segundo_numero, terceiro_numero):

    return (primeiro_numero + segundo_numero + terceiro_numero) / 3

resultado = mediaTresNumeros(20, 30, 50)

print(f"Resultado da media de três números: {resultado}")
