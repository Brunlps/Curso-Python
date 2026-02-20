
''''Função que faz a contagem regresiva'''
def regressiva(i):
    print(i)
    if i <= 1:
        return
    else: 
       return regressiva(i - 1)
regressiva(3)
''''Função que soma os valores'''
# def soma_recursiva(n):
#     # caso base
#     if n == 0:
#         return 0

#     # chamada recursiva
#     return n + soma_recursiva(n - 1)


# # entrada do usuário
# valor = int(input("Digite um número inteiro positivo: "))

# resultado = soma_recursiva(valor)

# print("Resultado da soma:", resultado)
