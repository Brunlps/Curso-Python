# Sistema de cadastro de alunos
curso_diponíveis = ("Java", "Python", "JavaScript")

lista_alunos = []

for i in range(3):
    nome_aluno = input("Nome: ")
    idade_aluno = input("Idade: ")

    curso_escolhido = int(input("""
                        ESCOLHA 1 CURSO
                        1 - Java
                        2 - Python
                        3 - JavaScript
                        Digite um número: """))

    if curso_escolhido == 1:
        # curso_aluno = "Java"
        curso_aluno = curso_diponíveis[curso_escolhido - 1]

    if curso_escolhido == 2:
        # curso_aluno = "Python"
        curso_aluno = curso_diponíveis[curso_escolhido - 1]

    if curso_escolhido == 3:
        # curso_aluno = "JavaScript"
        curso_aluno = curso_diponíveis[curso_escolhido - 1]

    dicionario_alunos = {
        'Nome': nome_aluno,
        'Idade': idade_aluno,
        'Curso': curso_aluno
    }

    if dicionario_alunos:
        lista_alunos.append(dicionario_alunos)

for aluno in lista_alunos:

    print(f"Nome: {aluno['Nome']} | Idade: {aluno['Idade']} | Curso: {aluno['Curso']}")

print(f"Foram: {len(lista_alunos)} alunos cadastrado")
