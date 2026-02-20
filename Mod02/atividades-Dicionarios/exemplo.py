# pessoas = {
#     'nome': 'Bruna',
#     'sexo': 'F',
#     'idade': 29
# }
# print(pessoas['nome'])
# print(pessoas['sexo'])
# print(pessoas['idade'])
# print('=' * 60)

# print(f'A {pessoas['nome']} é {pessoas['sexo']} e tem {pessoas['idade']}')
# print('=' * 60)

# print(pessoas.values())
# print(pessoas.keys())
# print(pessoas.items())
# print('=' * 60)


# del pessoas['sexo']

# print('=' * 60)

# for k, v in pessoas.items():
#     print(f'{k} = {v}')
# print('=' * 60)

# estado = dict()
# brasil = list()

# #Adiciona dicionário em listas
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federal: '))
#     estado['sigla'] = str(input('Sigla do Estado: '))
#     brasil.append(estado.copy())
    

# for e in brasil:
#     print('=' * 60)

#     for k, v in estado.items():
#         print(f'O campo {k}')
#         print(v , end = ' ')
        

# #print(brasil)

# estoque = {
#     "Tomate" : {
#         "qtd": 1000,
#         "valor": 2.30
#     },
#     "Cebola" : {
#         "qtd" : 500,
#         "Valor": 3.10
#     },
#     "Chuchu" : {
#         "qtd": 1000,
#         "valor": 2.30
#     },
#     "Batata" : {
#         "qtd" : 500,
#         "Valor": 3.10
#     },
#     "Pimentão" : {
#         "qtd": 1000,
#         "valor": 2.30
#     },
#     "Alho" : {
#         "qtd" : 500,
#         "Valor": 3.10
#     }


estoque = {
    "tomate" : [100, 2.30],
    "alface" : [500, 0.45],
    "batata" : [2001, 1.20],
    "feijao" : [100, 1.50]

}

vendas = [["Tomate", 5],["Batata", 3],["Pimentão", 8]]
total = 0
print("Vendas:\n")

for operacao in vendas:
    # 
    produto, quantidade = operacao
    
    preco = estoque[produto][1]
    
    custo = preco * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {operacao:6.2f} = {custo:6.2f}")
    estoque[produto[0]] -= quantidade
    total += custo

print(f"Custo total: {total:21.2f}\n")
print("Estoque:\n")

for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")