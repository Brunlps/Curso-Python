def wellcome():
    print("Hello World!")
    
# Chamando a função
wellcome()

# Função para somar 2 números
def sum():
    return 5 + 4
# chamando a função
print(sum())

# Atividade 01: Crie uma função 
# que receba dois argumentos( last name and fist name)

def full_name(last_name, fist_name):
    print(f"Nome Completo: {last_name} {fist_name}")

full_name("Bruna", "Lopes")

# Atividade 02: 
# Crie uma função que some dois números via parâmetro
def sum(a, b):
    print(f"A soma de {a} e {b} é: {a + b}")

number1 = int(input("Digite um número: "))   
number2 = int(input("Digite outro número: "))   
sum(number1, number2)

# Atividade 03:
# Crie uma funçõ que tenha um argumento default.
def address(country="Brasil."):
    print(f"Eu moro no {country}")
    
    
address("Canadá.")

