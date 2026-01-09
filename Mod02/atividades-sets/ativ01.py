'''Atividade 01: 
    Crie um conjunto vazio chamado frutas e adicione as 
    seguintes frutas a ele: "maçã", "banana", "uva", "laranja" e "morango". 
    Em seguida, imprima o conjunto.'''
    
# Conjunto vazio
frutas = set()

# Adiciona as frutas
frutas.add("maçã")
frutas.add("banana")
frutas.add("uva")
frutas.add("laranja")
frutas.add("morango")

print(frutas)

'''
    Atividade 02:
    Verifique se a fruta "banana" está presente no conjunto 
    frutas e imprima o resultado.'''
print("banana" in frutas)  

''' Atividade 3:

    Crie um conjunto chamado frutas_vermelhas e adicione
    as seguintes frutas a ele:
    "morango", "cereja" e "framboesa". 
    Em seguida, imprima o conjunto.'''
    
# Novo conjunto
frutas_vermelhas = {"morango", "cereja", "framboesa"}
print(frutas_vermelhas)

'''
    Atividade 4:
    Remova a fruta "cereja" do conjunto frutas_vermelhas e
    imprima o conjunto atualizado'''
    
frutas_vermelhas.remove("cereja")
print(f"Frutas vermelhas atualizadas: {frutas_vermelhas}")

'''
    Atividade 5:
    Crie doir conjunto, A e B, e realize a união dos dois conjunto.'''
    
A = {1, 2, 3}
B = {1, 6, 7}
print(f"A união dos conjuntos A e B: {A | B}")