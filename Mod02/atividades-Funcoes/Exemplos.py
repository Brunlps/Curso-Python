# ==== Programa 8.1 ====
"""
    Essa função tem como objetivo percorrer a lista usando o for e filtrar os 
    números que são iguais ao valor.
"""
# def pesquise(lista , valor):
#     for x, e in enumerate(lista):
#         if e == valor:
#             return x
    
# # Função que cacula a média
# def soma(l):
"""
    Essa função tem como objetivo soma os elementos da lista com a utilização
    do laço for para fazer esse calculo automaticamente, e no final vai retorna 
    a soma total desses elementos.
"""
#     total = 0
#     for e in l:
#         total += e
#     return total
# def media(l):
"""
    Essa função irar calcular a média de todos os elementos somados, e o retorno será esse claculo.
"""
#     return soma(l) / len(l)

l = [10, 20, 25, 30, 45]
# # print(pesquise(l, 25)) # Existe no índice 3
# # print(pesquise(l, 27)) # Não existe
# # print(media(l)) # Soma todos os números
# print(soma(l)) # Calcula a médsia dos números

# ==== Programa 8.2 ====
# Como não escrever uma função
def soma(l):
    """ 
    Essa função apenas vai somar os 5 primeiros números da lista, 
    o uso do laço while 
    será usado para encontrar esse 5 números e calcular eles
    """
    total = 0
    x = 0
    while x < 5:
        total += l[x]
        x += 1
    return total
print(soma([1, 2, 45, 200, 90, 34])) # 
print(soma(l))  

# ==== Programa 8.1 ====