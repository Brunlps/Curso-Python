# # Definição de lista
# lista_compras = [
#     "Arroz", 
#     "Feijão", 
#     "Leite", 
#     "Pão", 
#     "Óleo"]

# print("=" * 50)
# print("Lista de Compras", end='\n\n')

# # Percorrendo a lista de compras.
# for item in lista_compras:
#     print("[ ]", item)
    
# print("=" * 50)


# notas = [0,0,0,0,0]
# soma = 0
# x = 0
# while x < 7:
#     notas[x] = float(input(f"Notas {x}: "))
#     soma += notas[x]
#     x += 1
# print("Notas adicionadas com sucesso! ")

# x = 0
# while x < 7:
#     print(f"Notas {x}: {notas[x] : 6.2f}")
#     x += 1
# print(f"Média: {soma / x: 5.2f}")

# Progrma 6.3
# numeros = [0,0,0,0,0]
# x = 0

# while x < 5:
#     numeros[x] = int(input(f"Números {x + 1}: "))
#     x += 1
    


# while True:
#     escolhido = int(input(f"Que posição você quer imprimir (0 para sair): "))
    
#     if escolhido == 0:
#         print("Saindo!")
#         break
#     else:
        # print(f"Você escolheu o número: {numeros[escolhido - 1]}")
# programa 6.4
# l = [1,3,4,5,6]  
# x = 0      
# while x < len(l):
#     print(l[x])
#     x += 1

# =========================================================================================

# - Exercício 6.2: Faça uma programa que leia duas listas e 
# que gere uma terceira lista com os elementos das duas listas

# lista_nomes = ["Bruna", "João", "José"]
# lista_frutas = ["Manga", "pera", "Melão"]

# lista_coisas = []
# lista_aleatoria = []

# lista_aleatoria.append(lista_nomes)
# lista_aleatoria.append(lista_frutas)
# print(f"- Nessa lista foi utilizado o método .append:\n {lista_aleatoria}")

# print("=-" * 50)

# lista_coisas.extend(lista_frutas)
# lista_coisas.extend(lista_frutas)
# print(f" - Nessa lista foi utilizado o método .extend:\n {lista_coisas}")
# print("=-" * 50)

# =========================================================================================

# - Exercício 6.3: Faça um  progrma que percorra duas listas 
# e gere uma terceira lista sem elementos repetidos.

# lista_frutas = ['manga', 'pera', 'mamão']
# lista_frutas2 = ['laranja', 'goiaba', 'mamão']

# todas = lista_frutas + lista_frutas2

# listas_das_frutas = []


# x = 0
# # Percorre a lista
# while x < len(todas):
    
#     # Verifica se a elementos repetidos
#     if todas[x] not in listas_das_frutas:
#         # Adiciona cada elemento
#         listas_das_frutas.append(todas[x])
    
#     x += 1
# print("=-" * 50)

# print(f"Lista 1: {lista_frutas} e \nlista 2: {lista_frutas2} \nadicionadas com sucesso!")
# print(listas_das_frutas)


                    
            
            
            
            
            
            
            
            
            
# ultimo = 10
# # Fila começa por 1 e soma o numero do ultimo + 1, é tipo um incremento
# fila = list(range(1, ultimo + 1)) 

# while True:       
            
        # match operacao:
        #     case 1:
                
        #         ultimo += 1
        #         fila.append(ultimo)
                
                    
        #     case 2:
        #         if len(fila) > 0:
        #             atendido = fila.pop(0)
        #             print(f"Cliente {atendido} atendido.")
        #         else:
        #             print("Fila vazia! Nimguém para atender.")
            
        #     case 3:
        #         break
            # case _:
            #     print("Operação inválida! Digite apenas de 1 a 3!")
                    
            
