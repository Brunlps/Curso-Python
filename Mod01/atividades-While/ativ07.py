# A variavál vai contar de 1 a 10
contador = 0

# Uma variável para o usuário
numero_usuario = int(input('Digite uma número: '))

# Laço que inicia com contador 0 e termina em 10
while contador < 10:
    contador += 1
    #Concatena 1 + 1 = 2 | 1 + 2 = 3... | 1 + 9 = 10
    
    resultado = numero_usuario * contador
    #Multiplica numero do usuário pelo contador atualizado
    
    # Nessa condição, só apenas os números que forem multiplicados por 3
    # Serão exibidos para o usuário
    if resultado % 3 == 0:
        print(f'{contador} x {numero_usuario} = {resultado}')