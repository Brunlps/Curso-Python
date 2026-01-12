pessoas = {
    'nome': 'Bruna',
    'sexo': 'F',
    'idade': 29
}
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print('=' * 60)

print(f'A {pessoas['nome']} é {pessoas['sexo']} e tem {pessoas['idade']}')
print('=' * 60)

print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
print('=' * 60)


del pessoas['sexo']

print('=' * 60)

for k, v in pessoas.items():
    print(f'{k} = {v}')
print('=' * 60)

estado = dict()
brasil = list()

#Adiciona dicionário em listas
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federal: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    

for e in brasil:
    print('=' * 60)

    for k, v in estado.items():
        print(f'O campo {k}')
        print(v , end = ' ')
        

#print(brasil)

