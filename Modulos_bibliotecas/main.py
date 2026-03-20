from funcoes import *

while True:
    print("1 - Adicionar")
    print("2 - Mostrar")
    
    opcao = input("Escolha uma opção: ")
    
    
    match opcao:
        case "1":
            add_task()
            
        case "2":
            mostrar()
            
