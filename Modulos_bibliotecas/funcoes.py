lista_tarefa = []

def add_task():
    
    tarefa = input("Digite o nome da tarefa: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade: ")
        
    nova_tarefa = {
        "Tarefa": tarefa,
        "Descrição": descricao,
        "Prioridade": prioridade,
    }

    lista_tarefa.append(nova_tarefa)

def mostrar():
    if not lista_tarefa:
        print("Lista está vazia!")
    else:
        for i, element in enumerate(lista_tarefa):
            print(f"""
            {i+1} - {element['Tarefa']}
            Descrição: {element['Descrição']}
            Prioridade: {element['Prioridade']}

""")
