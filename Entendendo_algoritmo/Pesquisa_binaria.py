
def buscarMenor(arr):

    menor = arr[0]
    menor_indice = 0
    
    for i in range(1, len(arr)):

        if arr[i] < menor:
         menor = arr[i]
         print(menor)
         menor_indice = i
         print(menor_indice)
         
    return menor_indice

def ordenacaoSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscarMenor(arr)
        print(menor)
        novoArr.append(arr.pop(menor))
        print(novoArr)
    return novoArr

