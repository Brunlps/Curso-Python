# Crie um dicionário que irá armazenar informações de um contato, incluindo 
# o nome, o telefone e o email. 

    #  Peça ao usuário para fornecer esses dados, 
        # solicitando que ele insira o nome do contato, 
        # o número de telefone e o endereço de email. 
        # 
        # Após coletar todas as informações necessárias, 
        # exiba o conteúdo do dicionário, 
        # mostrando todas as informações do contato inserido pelo usuário.
        
name = input("Digite seu nome: ")
phone_number = int(input("Digite seu nome: "))
email = input("Digite seu nome: ")

contato = {
    "Nome": name,
    "Telefone": phone_number,
    "Email": email
}

print(f"- {contato["Nome"]}\n- {contato["Telefone"]}\n- {contato["Email"]}")
 
