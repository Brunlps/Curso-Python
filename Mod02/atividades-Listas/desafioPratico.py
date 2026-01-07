'''
    Suponha que você está gerenciando uma competição esportiva e tem
    uma lista de tuplas representando os resultados das equipes em
    diferentes modalidades. Cada tupla contém o nome da equipe, seguido
    por uma lista de pontuações obtidas em cada rodada da competição.

    1.Calcule a média das pontuações de cada equipe e armazene esses
    valores em uma nova lista chamada medias.
    
    2.Ordene a lista medias em ordem decrescente.
    
    3.Crie uma nova lista chamada classificacao que contém tuplas, onde
    cada tupla contém o nome da equipe e sua média de pontuações.
    
    4.Exiba na tela a classificação final das equipes, mostrando o nome da
    equipe e sua média, da equipe com a pontuação mais alta para a
    mais baixa.
'''
# Nome da equipe
equipe_nova1 = 'Dormi nenem'
equipe_nova2 = 'Bombe pac'
#Pontos da equipe
pontos_eq1 = (9, 10, 23)
pontos_eq2 = (8, 140, 20)


# 1.Calcule a média das pontuações de cada equipe e armazene esses
# valores em uma nova lista chamada medias.
    # Calculamdo a média dos pontos
media_pontos1 = sum(pontos_eq1) / len(pontos_eq1)
media_pontos2 = sum(pontos_eq2) / len(pontos_eq2)



# 2.Ordene a lista medias em ordem decrescente.
lista_pontos_nova = [media_pontos1, media_pontos2]
print(lista_pontos_nova)



# 3.Crie uma nova lista chamada classificacao que contém tuplas, onde
# cada tupla contém o nome da equipe e sua média de pontuações.#
    # Tupla com nome e pontos da equipe
equipe01 = (equipe_nova1, media_pontos1)
equipe02 = (equipe_nova2, media_pontos2)

#Armazenando em uma lista
classificacao = [
    (equipe_nova1, media_pontos1),
    (equipe_nova2, media_pontos2)
]
print(classificacao)

# Ordenar pela média (posição 1 da tupla)
# Ela organiza os times pela nota, do maior para o menor.
classificacao.sort(key=lambda x: x[1], reverse=True)
print(classificacao)

# Exibir a classificação final

print('Classificação final:')
for equipe, media in classificacao:
    print(f'Equipe: {equipe} | Média: {media:.2f}')