task_list = []



# Função criar tarefas
def new_tasks(name=str, description=str, category=str,priority=str, status=str):
    
    name = input("Tarefa:\n")
    description = input("Descrição:\n ")
    category = input("Categoria:\n")
    status = "Em andamento."
    while True:
        
        opcao = input("""
    =-=-=-=-=-=PRIORIDADE=-=-=-=-=-=
    
            1 - BAIXA
            2 - MÉDIA
            3 - ALTA
        
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    \nESCOLHA UMA OPÇÃO: """)
        
        
        if opcao not in ["1", "2", "3"]:
            print("Escolha uma opção válida!")           
            
        else:    
            match opcao:
                case "1":
                    priority = "BAIXA"
                    break
                case "2":
                    priority = "MÉDIA"
                    break
                case "3":
                    priority = "ALTA"
                    break
    new_task = {
        "Tarefa": name,
        "Descrição": description,
        "Categoria": category,
        "Prioridade": priority,
        "Status":status
    }
    task_list.append(new_task)
    
    
# ================================================================================================    
# Função que exibi todas as tarefas
def display_tasks():
    if not task_list:
        print("Lista está vazia!")
    else:
        for i, element in enumerate(task_list):
            print(f"""
            {i+1} - {element['Tarefa']}
            Descrição: {element['Descrição']}
            Categoria: {element['Categoria']}
            Prioridade: {element['Prioridade']}
            Status: {element['Status']}
""")
            
# ================================================================================================
# Função para concluir tarefa
def  task_status():
    indice = int(input("Digite o número da tarefa: ")) - 1

    if 0 <= indice < len(task_list):
        tarefa = task_list[indice]
        tarefa["Status"] = "Concluído."
        print(f"Tarefa '{tarefa['Tarefa']}' foi concluída com sucesso!")
    else:
        print("Tarefa não encontrada.")


# ================================================================================================
# Função para filtrar categoria
def filter_category():
    category = input("Digite a categoria que deseja buscar: ")
    result = []

    for task in task_list:
        if task["Categoria"].lower() == category.lower():
            result.append(task)

    if not result:
        print("Nenhuma tarefa encontrada nessa categoria.")
    else:
        print("\nTarefas encontradas:\n")

        for task in result:
            print(f"Tarefa: {task['Tarefa']}")
            print(f"Descrição: {task['Descrição']}")
            print(f"Categoria: {task['Categoria']}")
            print(f"Prioridade: {task['Prioridade']}")
            print(f"Status: {task['Status']}")
            print("-" * 30)    
    
# ================================================================================================ 
# Função para filtrar Prioridade
def filter_priority():
    priority = input("Digite a prioridade (BAIXA, MÉDIA, ALTA): ")
    result = []

    for task in task_list:
        if task["Prioridade"].lower() == priority.lower():
            result.append(task)

    if not result:
        print("Nenhuma tarefa encontrada com essa Prioridade.")
    else:
        print("\nTarefas encontradas:\n")
        for task in result:
            print(f"Tarefa: {task['Tarefa']}")
            print(f"Descrição: {task['Descrição']}")
            print(f"Categoria: {task['Categoria']}")
            print(f"Prioridade: {task['Prioridade']}")
            print(f"Status: {task['Status']}")
            print("-" * 30) 
    
# ================================================================================================
# Funçào para exibir Menu
def display_menu():
    print("\n1 - Adicinar tarefa")
    print("2 - Listar tarefas")
    print("3 - Filtrar Categoria")
    print("4 - Filtrar Prioridade")
    print("5 - Marca concluído") 


# ================================================================================================
# Função de encerrar o sistema
def main():
    while True:
        display_menu()
        opcao = input("\nEscolha uma opção: ")
        
    
        match opcao:
                case "1":
                    # Adicinar nova tarefa
                    new_tasks()
                case "2":
                    # Verificar tarefas
                    display_tasks()
                    
                case "3":
                    filter_category()
                    
                case "4":
                    filter_priority()
                    
                case "5":
                    task_status()
                    
                case "0":
                    print("Você escolheu a opção de sair.")
                    print("Saindo...")
                    break
        
main()