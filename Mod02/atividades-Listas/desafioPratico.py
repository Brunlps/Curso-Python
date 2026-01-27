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
menu = input('''========== Menu ==========
             1 - Cadatrar Equipe
             2 - Médoia de pontpo por equipe
             3 - Classificação das equipes
             4 - Sair
             ''')
lista_equipes = []
match menu:
    case '1':
        
    # Nome da equipe
        equipe_nova = input('Digite o nome da equipe: ')
        lista_equipes.append(equipe_nova)
        print('Equipe adicionada com sucesso!')
        
        #Pontos da equipe
        while equipe_nova in lista_equipes:
            qtd_pontos_equipe = int(input('A equipe tem quantos pontos: '))
            
            if qtd_pontos_equipe == qtd_pontos_equipe:
                for i in range(qtd_pontos_equipe):
                    pontos_novos = int(input('Digite um ponto: '))
                    # pontos_novos += pontos_novos
                    equipe_nova = pontos_novos
                    lista_equipes.append(equipe_nova)
                    if i == qtd_pontos_equipe:
                        print('Pontos adicionados com sucesso!')
                print(f'Equipe{lista_equipes[1]} {lista_equipes}')
            break

# # 1.Calcule a média das pontuações de cada equipe e armazene esses
# # valores em uma nova lista chamada medias.
#     # Calculamdo a média dos pontos
# media_pontos1 = sum(pontos_eq1) / len(pontos_eq1)
# media_pontos2 = sum(pontos_eq2) / len(pontos_eq2)



# # 2.Ordene a lista medias em ordem decrescente.
# lista_pontos_nova = [media_pontos1, media_pontos2]
# print(lista_pontos_nova)



# # 3.Crie uma nova lista chamada classificacao que contém tuplas, onde
# # cada tupla contém o nome da equipe e sua média de pontuações.#
#     # Tupla com nome e pontos da equipe
# equipe01 = (equipe_nova1, media_pontos1)
# equipe02 = (equipe_nova2, media_pontos2)

# #Armazenando em uma lista
# classificacao = [
#     (equipe_nova1, media_pontos1),
#     (equipe_nova2, media_pontos2)
# ]
# print(classificacao)

# # Ordenar pela média (posição 1 da tupla)
# # Ela organiza os times pela nota, do maior para o menor.
# classificacao.sort(key=lambda x: x[1], reverse=True)
# print(classificacao)

# # Exibir a classificação final

# print('Classificação final:')
# for equipe, media in classificacao:
#     print(f'Equipe: {equipe} | Média: {media:.2f}')