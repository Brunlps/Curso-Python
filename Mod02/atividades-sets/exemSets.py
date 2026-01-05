meu_set = {'infinity', 'School'}
print(type(meu_set))

# Sets de frutas, não é permitido duplicatas de elementos
frutas =  {'maçã', 'banana', 'cereja', 'maçã'}
print(frutas)

# 2. Usando Compreensão de Conjuntos:
set1 = {letra for letra in 'infinity' if letra not in 'aeiou'}
print(set1)

# 3. Usando o método Construtor:
set2 = set(['infinity', 'School'])
print(set2)

# Adicionando itens no SET
convidados = {'bruna', 'janaina', 'joão'}
print(convidados)

# Método para adicionar elementos: .add()
convidados.add('pedro')
print(convidados)

# Método para adicionar um conjunto ao set
ids = {'12', '63', '14'}
print(ids)
novos_ids = {'100', '54', '87'}
print(novos_ids)

# Método UPDATE, é usado para juntar conjunto de elementos.
ids.update(novos_ids)
print(f'Junção dos conjuntos: {ids}')