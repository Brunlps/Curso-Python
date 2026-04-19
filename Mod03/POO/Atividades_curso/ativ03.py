# Crie uma classe Empresa que permita gerenciar
# funcionários. Os funcionários devem ter informações
# como nome, cargo e salário. A empresa deve ser capaz
# de adicionar, remover e listar funcionários.

class Empresa:
    def __init__(self, name: str, position: str, salary: float, lista_funcionarios: list, funcionarios: dict):
        self.name = name
        self.position = position
        self.salary = salary
        self.lista_funcionarios = lista_funcionarios
        self.funcionarios = funcionarios

    
    def adicionar_funcionarios(self):
        self.name = input("Digite seu nome: ")
        self.position = input("Digite seu nome: ")
        self.salary = input("Digite seu nome: ")

        print("Dados Cadastrados com sucesso!")
    
    def remover(self):
        