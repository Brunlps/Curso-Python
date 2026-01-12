'''
    Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.'''
livro = {
    'Nome': 'Anne Frank',
    'Genero': 'Drama',
    'Preço': 100   
}

# Percorrer o dicionário
for k, v in livro.items():
    print(f'A chave é {k} e o valor é {v}.')
    
    
# .items() -> Mostra chave e valor 
# .values() -> Mostra os valores 
# .keys() -> Mostra as chaves