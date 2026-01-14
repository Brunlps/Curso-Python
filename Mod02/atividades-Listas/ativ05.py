# 🧠 Exercício 1 — Criando uma lista do zero

    # Crie uma lista vazia chamada numeros.
    # Peça ao usuário para digitar 5 números e vá adicionando cada um na lista.
    # No final, mostre a lista completa.
    
numeros = []

for i in range(1, 6):
    numero = int(input(f"Digite o {i}° número:"))
    numeros.append(numero)
  
print(f"Lista de números adicionado: {numeros} ")