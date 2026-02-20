# Programa 6.7: Simulação de uma fila de banco

# Programa 6.7: Simulação de uma fila de banco
ultimo = 10
# Fila começa por 1 e soma o numero do ultimo + 1, é tipo um incremento
fila = list(range(1, ultimo + 1)) 
rodando = True
while True:
    
    print(f"\nExiste {len(fila)} clientes na fila.")
    
    operacao = input(""" 
        =-=-=-=-=-=-=-=-=-= Menu =-=-=-=-=-=-=-=-=-==-=-=
                1 - Para realizar o atendimento.
                2 - Adicionar um cliente ao fim da fila. 
                3 - Para sair.
        =-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=\n
                Escolha uma opção: """)
    
    x = 0
    while x < len(operacao):
        if operacao == "1":
            
            if len(fila) > 0:
                atendimento = fila.pop(0)
                print(f"Cliente {atendimento} atendido.")
            else:
                print("Fila vazia! Nimguém para atender.")
                
        elif operacao == "2":
            ultimo += 1
            fila.append(ultimo)
            
        elif operacao == "3":
            print("Saindo do programa...")

            break
    
        else:
            print("Operação inválida! Digite apenas de 1 a 3!")
        









# Programa 6.7 modificado para receber varias str: Simulação de uma fila de banco
# Programa 6.7: Simulação de uma fila de banco
# ultimo = 10
# # Fila começa por 1 e soma o numero do ultimo + 1, é tipo um incremento
# fila = list(range(1, ultimo + 1)) 
# rodando = True
# while rodando:
    
#     print(f"\nExiste {len(fila)} clientes na fila.")
    
#     operacao = input(""" 
#         =-=-=-=-=-=-=-=-=-= Menu =-=-=-=-=-=-=-=-=-==-=-=
#                 1 - Para realizar o atendimento.
#                 2 - Adicionar um cliente ao fim da fila. 
#                 3 - Para sair.
#         =-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-==-=-=-=-=-=\n
#                 Escolha uma opção: """)
    
#     x = 0
#     while x < len(operacao):
#         opcao = operacao[x]
        
#         if opcao == "1":
            
#             if len(fila) > 0:
                
#                 atendimento = fila.pop(0)
#                 print(f"Cliente {atendimento} atendido.")
#             else:
#                 print("Fila vazia! Nimguém para atender.")
                
#         elif opcao == "2":
#             ultimo += 1
#             fila.append(ultimo)
            
#         elif opcao == "3":
#             print("Saindo do programa...")
#             rodando = False
#             break
    
#         else:
#             print("Operação inválida! Digite apenas de 1 a 3!")
        
#         x += 1