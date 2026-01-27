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
    
    4.Exiba na tela a , da equipe com a pontuação mais alta para a
    mais baixa.
'''

'''
 - Lista_equipes = [ tuplas_equipes = ()]
 - tuplas_equipe = (
     'Nome'
     lista_pontos = [Rodada 1 -> p1, Rodada 2 -> p2, Rodada 3 -> p3]
 )
 
 - Calculando_media = soma/lista_pontos
 - Ordenando uma lista -> .Reverse()
 - Lista_classificação = Nome_equipe : Pontos
 - Pontuação Do maior para o menor
'''

while True:
    lista_Equipes = []
    Lista_classificacao = []
    pontos_equipes = []
    
    menu = input('''================Menu=================
                 1 - Cadastra Equipe
                 2 - Ver Equipes
                 3 - Calcular média da equipe
                 ''')
    
    match menu:
        case '1':
            modaalidade = ('Digite a modalidade: ')
            nome_equipe = input('Digite o nome da equipe: ')
            qdt_pontos = int(input('Deseja adicionar os ponto(1 - Sim/2 - Não): '))
            #Pedindo os pontos da equipe:
            if qdt_pontos > 0:
                
                posto_da_equipe = int(input('Digite o ponto: '))
            
        # case '2':
        # case '3':