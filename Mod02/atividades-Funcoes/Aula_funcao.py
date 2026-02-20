# AULA 04 - PYTHON - FUNÇÕES

# ATIVIDADE DE REVISÃO
# FAÇA UM PROGRAMA QUE PERMITE O USUÁRIO:
# ADICIONAR POKEMON
# 1.1 - NOME, TIPO
# 2 - VER TODOS OS POKEMONS
# 3 - VER POKEMONS POR TIPO
# 4 - EXCLUIR POKEMON
# 0 - SAIR

lista_pokemons = []
while True:
  menu = input("""
  ESCOLHA UMA OPÇÃO:
  1-  ADICIONAR POKEMON
  2 - VER TODOS OS POKEMONS
  3 - VER POKEMONS POR TIPO
  4 - EXCLUIR POKEMON
  0 - SAIR
  """)
  match menu:
    case '1':
      print("=-=-= TELA DE CADASTRO =-=-=-=")
      nome = input("Digite o nome do novo pokemon: ")
      tipo = input("Digite o tipo do novo pokemon: ")
      novo_pokemon = {
        "Nome": nome,
        "Tipo": tipo
      }
      lista_pokemons.append(novo_pokemon)
      print(f"Pokemon {nome} adicionado com sucesso.")
    case '2':
      if len(lista_pokemons) == 0:
        print("Nenhum pokemon cadastrado")
      else:
        print("=-=-=-= LISTA DE POKEMONS =-=-=-=-=")
        for element in lista_pokemons:
          print(f"{element['Nome']} - |{element['Tipo']}|")
    case '3':
      if len(lista_pokemons) == 0:
        print("Nenhum pokemon cadastrado")
      else:
        print("=-=-=-= FILTRO DE POKEMONS POR TIPO =-=-=-=")
        tipo_escolhido = input("Digite o tipo que você quer buscar: ")
        pokemons_encontrados = 0
        for element in lista_pokemons:
          if element['Tipo'].lower() == tipo_escolhido.lower():
            print(f"{element['Nome']} - |{element['Tipo']}|")
            pokemons_encontrados += 1
        if pokemons_encontrados == 0:
          print(f"Não existe nenhum pokemon do tipo {tipo_escolhido}")
    case '4':
      if len(lista_pokemons) == 0:
        print("Nenhum pokemon cadastrado")
      else:
        print("=-=-=-= TELA DE EXCLUSÃO DE POKEMON =-=-=-=")
        pokemon_excluido = input("Digite o nome do pokemon que você deseja deletar: ")
        pokemons_encontrados = 0
        for element in lista_pokemons:
          if element['Nome'].lower() == pokemon_excluido.lower():
            lista_pokemons.remove(element)
            pokemons_encontrados += 1
            print(f"Pokemon {element['Nome']} deletado com sucesso")
        if pokemons_encontrados == 0:
          print(f"Não existe nenhum pokemon chamado {pokemon_excluido}")
    case '0':
      break
    case _:
      print("DIGITA DIREITO BAITOLA")


# FUNÇÕES

def cumprimentar(nome):
  return f"Olá {nome}"

print(cumprimentar(nome="João"))
print(cumprimentar(nome="Maria"))
print(cumprimentar(nome="Abel"))
def checarIdades(idade):
  if idade >= 18:
    return "Maior de idade"
  else:
    return "Menor de idade"


idade = int(input("Digite uma idade: "))
print(checarIdades(idade=idade))

for i in range(5):
  nova_idade = int(input("Digite a nova idade"))
  print(checarIdades(idade=nova_idade))




lista_pokemons = []

def addPokemon():
  print("=-=-= TELA DE CADASTRO =-=-=-=")
  nome = input("Digite o nome do novo pokemon: ")
  tipo = input("Digite o tipo do novo pokemon: ")
  novo_pokemon = {
          "Nome": nome,
          "Tipo": tipo
        }
  lista_pokemons.append(novo_pokemon)
  return f"Pokemon {nome} adicionado com sucesso."

#SE A FUNÇÃO TIVER PRINTANDO UM FOR TU NÃOOOOOOOOOOOOOOOOOOO VAI TROCAR POR RETURN
def mostrarPokemons(): 
  if len(lista_pokemons) == 0:
    print("Nenhum pokemon cadastrado")
  else:
    print("=-=-=-= LISTA DE POKEMONS =-=-=-=-=")
    for element in lista_pokemons:
      print(f"{element['Nome']} - |{element['Tipo']}|")


def mostrarPorTipo():
  if len(lista_pokemons) == 0:
    print("Nenhum pokemon cadastrado")
  else:
    print("=-=-=-= FILTRO DE POKEMONS POR TIPO =-=-=-=")
    tipo_escolhido = input("Digite o tipo que você quer buscar: ")
    pokemons_encontrados = 0
    for element in lista_pokemons:
      if element['Tipo'].lower() == tipo_escolhido.lower():
        print(f"{element['Nome']} - |{element['Tipo']}|")
        pokemons_encontrados += 1
    if pokemons_encontrados == 0:
      print(f"Não existe nenhum pokemon do tipo {tipo_escolhido}")


def deletarPokemon():
  if len(lista_pokemons) == 0:
    return "Nenhum pokemon cadastrado"
  else:
    print("=-=-=-= TELA DE EXCLUSÃO DE POKEMON =-=-=-=")
    pokemon_excluido = input("Digite o nome do pokemon que você deseja deletar: ")
    pokemons_encontrados = 0
    for element in lista_pokemons:
      if element['Nome'].lower() == pokemon_excluido.lower():
        lista_pokemons.remove(element)
        pokemons_encontrados += 1
        return f"Pokemon {element['Nome']} deletado com sucesso"
    if pokemons_encontrados == 0:
      return f"Não existe nenhum pokemon chamado {pokemon_excluido}"

while True:
  menu = input("""
  ESCOLHA UMA OPÇÃO:
  1-  ADICIONAR POKEMON
  2 - VER TODOS OS POKEMONS
  3 - VER POKEMONS POR TIPO
  4 - EXCLUIR POKEMON
  0 - SAIR
  """)
  match menu:
    case '1':
      print(addPokemon())
    case '2':
      mostrarPokemons()
    case '3':
      mostrarPorTipo()
    case '4':
      print(deletarPokemon())
    case '0':
      break
    case _:
      print("DIGITA DIREITO BAITOLA")

# CÓDIGO DE ALUNO
pokemons = []

while True:
    opcao = input("""
-=-=-=-=-=-=-=-=-=-=-=-=-
Digite uma opção:
1 - Adicionar Pokémon
2 - Ver todos os Pokémons
3 - Ver Pokémons por tipo
4 - Excluir Pokémon
0 - Sair
-=-=-=-=-=-=-=-=-=-=-=-=-
> """)
    
    match opcao:
        case "1":
            nome = input("Nome do Pokémon: ")
            tipo = input("Tipo: ")

            pokemon = {
                "Nome": nome,
                "Tipo": tipo
            }

            pokemons.append(pokemon)
            print(f"Pokémon {pokemon} adicionado com sucesso!")
        
        case "2":
            for pokemon in pokemons:
                print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-
Nome: {pokemon['Nome']}
Tipo: {pokemon['Tipo']}
-=-=-=-=-=-=-=-=-=-=-=-=-
""")
        case "3":
            pesquisarTipo = input("Digite o tipo de quais Pokémons deseja ver: ")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-")
            for pokemon in pokemons:
                if pokemon["Tipo"] == pesquisarTipo:
                    print(f"""
Nome: {pokemon['Nome']}
Tipo: {pokemon['Tipo']}
""")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-")
        
        case "4":
            deletar = input("Digite corretamente o nome do Pokémon que deseja excluir: ")
            for pokemon in pokemons:
                if deletar == pokemon['Nome']:
                    pokemons.remove(pokemon)
                    print("Pokémon removido com sucesso!")

        case "0":
            break
        
        case _:
            print("Valor inválido!")