
# ATIVIDADE PRÁTICA 10

# Desenvolva um programa que recebe um dicionário, uma
# chave e um valor como entrada e adiciona a chave e o
# valor ao dicionário, atualizando o valor se a chave já
# existir.

# 01 - Cadastro de pessoas
# Se a pessoa não for cadastrada, crie uma nova entrada de dados.
# Se essa pessoa já tem cadastro, so adicione o valor a chave da pessoa

cadastro_pessoas = [
    
    {
    "Nome": 'Bruna',
    "Idade": 30
    },
    
    
    {
    "Nome": 'Lopes',
    "Idade": 20
    },
    
    {
    "Nome": 'João',
    "Idade": 15
    },
    
   {
    "Nome": 'Ben',
    "Idade": 13
    }
]

for keys, values in cadastro_pessoas.count():
    
    print(f"Nome: {keys}")


# print(type(cadastro_pessoas))

# Método para usar:
    # Adicionando um valor a chave
    # dicionario[chave] = Novo_valor