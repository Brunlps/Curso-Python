# Cria um dicionário com os dados de uma pessoa,
# com as chaves nome, idade e cidade.
# Depois acesse e imprima cada valor separadamente.


pessoa1 = {
    'Nome': "Bruna Lopes",
    'Idade': 35,
    'Cidade': "Fortaleza"
}
print(pessoa1)

for chave, itens in pessoa1.items():
    # print(chave, ": ", itens)
    print(f"{chave}: {itens}")
