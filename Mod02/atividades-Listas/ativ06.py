# 🧠 Exercício 2 — Cadastro de nomes

# Crie uma lista vazia chamada nomes.
# Peça ao usuário para digitar nomes até que ele digite "sair".
# Quando isso acontecer, mostre todos os nomes cadastrados.
nomes = []
while True:
    #Entrada
    nome = input('Digite um nome: ')
    #verifica quer sair...
    if nome == 'sair' :
        break
    #Guarda apenas o nomes que foram adicionado anteriomente
    # Antes do usuário pedir para sair.
    nomes.append(nome)
#Mostrando os nomes.    
print(f'Lista de nomes: {nomes}')