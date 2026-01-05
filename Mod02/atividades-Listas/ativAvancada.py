
usuarios = []
linha = "=" * 50
#Controle de menu
while True:
    
    menu = input("""
        ================= Menu =================)
                1 - Adicionar\n
                2 - Verificar usuário\n
                3 - Atualizar usuário\n
                4 - Excluir usuário\n
                5 - Sair
                Escolha uma opção: 
        ========================================
        \n""")
    
    match menu:
        #Cadastrar um novo usuário.
        case "1":
            #Solicitando novos dados.
            nome = input("Digite seu nome: ").title()
            email = input("Digite seu email: ")
            
            print(linha)

            usuarios.append([nome, email])
            print(f"Nome: {nome}, \nEmail: {email}")
        
        #Verificar o usuário
        case "2":
            procurar = input("Digite o nome que deseja encontrar: ").title()
            encontrado = False
            
            for usuario in usuarios:
                if usuarios == procurar:
                    print("Usuário encontrado:")
                    print(f"Nome: {usuario[0]}")
                    print(f"Email: {usuario[1]}")
                    print("=" * 60)
                    encontrado = True
                    break
            if not encontrado:
                print("Usuário não encontrado!")
        
        # Atualiza os dados do usuário
        case "3":
            procurar = input("Digite o nome do usuário: ").strip().title()
            encontrado = False

            for usuario in usuarios:
                if len(usuario) >= 2 and usuario[0] == procurar:

                    encontrado = True

                    print("O que você deseja atualizar?")
                    print("1 - Nome")
                    print("2 - Email")
                    escolha = input("Escolha: ")


                    # Atualizar nome
                    if escolha == "1":
                        novoNome  = input("Digite o novo nome: ").title()
                        usuario[0] = novoNome
                        print("Nome atualizado com sucesso!")
                        print(linha)
                        
                    # Atualizar email
                    elif escolha == "2":
                        novoEmail = input("Digite o novo email: ")
                        usuario[1] = novoEmail
                        print("Email atualizado com sucesso!")
                        print(usuario)
                        print(linha)


                    break  # sai do for assim que atualizar
            else:
                print("Usuário não encontrado!")
                
        #Exclui o cadastro do usuário
        case "4":
            usuariosRemover = input("Qual o novo do usuário que deseja remover? ").title()
            encontrado = False
            removendo = None
            #Percorrendo pelo lista     
            for usuario in usuarios:
                
                #Verifica se o usuário foi encontrado
                if usuario[0] == usuariosRemover:
                    print("Encontrado!")
                    print(f"Usuário: {usuario}")
                    removendo = usuario
                    break
            else:
                print("Não encotrado!") 
                # volta ao menu sem tentar remover
                continue  
            # remover com segurança (só chega aqui se encontrado == True)        
            usuarios.remove(removendo)
            print(f"usuário pagado!")
        #Encerra o programa    
        case "5":
            print("Programa encerrado!")
            break
        
        #Erro para entradas inválidas
        case _:
            print("Entrada inválida!")
    