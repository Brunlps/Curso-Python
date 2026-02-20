a = 5 # Variável global
def muda_e_imprime():
    global a
    a = 7 # Variável interna
    print(f"A dentro da função: {a}")

print(f"a antes de mudar: {a}")
muda_e_imprime()
print(f"a depois de mudar: {a}")



"""
    Variáveis Globais:
    -> Letras maiúculas
    -> Usando intrução: global que a função acesse essa variável
    -> São usadas para configuração do programa e que seja constantes.
"""
EMPRESA = "Unidos Venceremos Ltda"
def imprime_cabecalho():
    print(EMPRESA)
    print(" - " * len(EMPRESA))
imprime_cabecalho()