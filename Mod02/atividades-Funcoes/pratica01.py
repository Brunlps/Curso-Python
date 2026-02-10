# Atividade prática 01:
    # Crie uma função que receba um nome e imprima uma saudação personalizada.
nome = input("Digite oa seu nome: ")
def saudacao(nome):
    """_função Saudação_

    Args:
        nome (string): Esse argumento recebe o nome do usuário é fomato de string.

    Returns:
        string: f-string coma mensagem personalezada com argumento.
    """
    return f"Seja bem vindo! {nome}."
    
print(saudacao(nome))