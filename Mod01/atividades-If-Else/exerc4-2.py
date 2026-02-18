velocidade_usuario = int(input("Digite a velocidade do seu carro: "))

if velocidade_usuario > 80:
    velocidade_usuario -=80
    velocidade_usuario *= 5
    print(f"Você foi multado! \nValor da multa: R${velocidade_usuario}")
if velocidade_usuario <= 80:
    print("Velocidade permitida!")