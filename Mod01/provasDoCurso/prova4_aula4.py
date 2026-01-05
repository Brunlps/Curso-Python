"""1
[LPIA-A04] Você está desenvolvendo um programa em Python para calcular 
a soma dos números pares dentro de um intervalo determinado pelo usuário. 
O programa deve solicitar ao usuário que insira dois números inteiros, 
representando o início e o fim do intervalo (inclusive).

Utilize um loop 'for' para iterar sobre todos os números no intervalo e 
somar apenas os números pares. Implemente a estrutura 'else' para exibir uma 
mensagem indicando que não há números pares no intervalo, caso seja o caso.

Ao final, exiba a soma dos números pares encontrados.

"""
# Entrada de dados do usuário.
numeroContagem1 = int(input("Digite um para iniciar a contagem: "))
numeroContagem2 = int(input("Digite outro número para o fim da contagem: "))
element = 0
soma = 0
#Verifica se os números digitados estão em ondem crescente
if numeroContagem1 < numeroContagem2:
    # Percorri e guarda o números na variável "element"
    for element in range(numeroContagem1, numeroContagem2):
        # Verifica os elemento que são pares
        if element % 2 == 0:
            print(f"Número par encontrado: {element}")
            soma += element # Soma cada número percorrido
            

    print(f"A soma dos números pares de {numeroContagem1} a {numeroContagem2} é: {soma}")        

else:
    print("O intervalo informado não está em ordem crescente.")