# Estrutura de dados SETS
'''
🧠 Encontrar vs acessar (diferença importante!)

🔎 Encontrar → verificar se algo existe (in)

📍 Acessar por índice → pegar pela posição ([0])

👉 Em sets, você encontra, mas não acessa por índice.

🎈 Frase perfeita para prova ou explicação

Sets não são ordenados e não possuem índices, portanto seus 
elementos não podem ser acessados ou modificados por posição.

🧠 Resumão rápido

Set ❌ não tem índice

Set ❌ não acessa por posição

Set ✅ verifica existência por valor

Set ❌ não modifica elemento individual por índice
'''

numbers = [1, 2, 3, 4]
#print(f'Lista de numeros:{numbers}')

set1 = set(numbers)
#print(set1)


set2 = {3, 4, 5}

# União
print(set1 | set2)# União de elementos

# Interseção
print(set1 & set2)# O que existe nos dois lugares ao mesmo tempo?

# Diferença
print(set1 - set2)# O que tem só aqui, mas não lá?

# Diferenças Simétricas
print(set1 ^ set2)# O que é exclusivo de cada um?

# Para saber se uma elemnto esta no conjunto

convidados = {'João', 'Maria', 'Eduarda'}

print('Maria' in convidados)

# Passar por cada elemento do conjunto
i = 0
for convidado in convidados:
    i += 1
    print(f'Convidado {i}: {convidado}')