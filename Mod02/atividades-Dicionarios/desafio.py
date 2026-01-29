# DESAFIO FINAL
# FAÇA UM PROGRAMA QUE PERMITE UM USUÁRIO ESCOLHER UMA OPÇÃO ENTRE:
# 1 - ADICIONAR NOVO PRODUTO
# 1.1 - NOME, PREÇO, QTDE_ESTOQUE.
# 2 - VER TODOS OS PRODUTOS
# 3 - EXCLUIR PRODUTO
 # Lista vazia
produto_registrado = []
while True:
    # Opção de escolha 
    # usando um tratamento de erro, caso o usuário digite 
    # o que esta fora do escopo.
    try:
        menu = int(input("""
                        =================Menu====================
                            =   1 - ADICIONAR NOVO PRODUTO    =
                            =   2 - VER TODOS OS PRODUTOS     =
                            =   3 - EXCLUIR PRODUTO           =
                            =   4 - SAIR                      =
                        =========================================
                        Escolha um opção: """))
        
        if menu < 1 or menu > 4:
            print("Escolha uma opção entre 1 e 4")
            continue
        
    except ValueError:
        print("Digite apenas números.")
        continue
    
   
    # MENU
    match menu:
        # Registro de produtos
        case 1: 
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            qtd_estoque = int(input("Digite o quantidade no estoque: "))
            
            
            # dicionario de cada produto.
            novo_produto = {
                "Nome": nome,
                "Preco": preco,
                "Quantidade em estoque": qtd_estoque
            }
            # Adicionando os produtos a uma lista
            produto_registrado.append(novo_produto)

            # Condiciona que verifica se o produto foi adicionado.
            if novo_produto in produto_registrado:
                print("Produto adicionado com sucesso!")
                
        case 2:
            # Ver todos os produtos.
            for element in produto_registrado:
                print(f"""
                    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                    INFORMAÇÃO DOS PRODUTOS:
                    
                    - {element["Nome"]}
                    - {element["Preco"]}
                    - {element["Quantidade em estoque"]}
                    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                """)
        # Caso para remover um produto.
        case 3:
            for produto in produto_registrado:
            
                print(f"""
                    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                    INFORMAÇÃO DOS PRODUTOS:
                    
                    {produto["Nome"]}
                    
                    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                """)
            
            opcao_produto_remover = input("Escolha um produto: ")
    
            for produto in produto_registrado:
                if produto["Nome"] == opcao_produto_remover:
                    produto_registrado.remove(produto)
                    print(f"{produto['Nome']} removido com sucesso!")
                    break
            else:
                print("Produto não encontrado.")
        case 4:
            if menu == 4:
                print(f"finalizando o programa... ")        
                print(f"Saindo.. ")
                break      
                