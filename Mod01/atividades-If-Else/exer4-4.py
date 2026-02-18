# Entrada para o salário do usuário
salario_usuario = float(input("Digite o valor do seu salário para saber o aumento: "))
base = salario_usuario
# Aumento de 10% para salários 1.250
aumento_10_porcent = 0.10

# Aumento de 15% para salários 1.250 ou abaixo desse valor.
aumento_15_porcent = 0.15

aumento = 0

if base > 1250:
    aumento = aumento + ((base + 1250) * aumento_10_porcent)
    base = 1250
    print(f"Salário: R${salario_usuario:6.2f}\nAumento: R${aumento}\nPorcento: {aumento_10_porcent}\nTotal: {salario_usuario + aumento}")
elif base <= 1250:
    aumento = aumento + ((base + 1250) * aumento_15_porcent)
    print(f"Salário: R${salario_usuario:6.2f}\nAumento: R${aumento}\nPorcento: {aumento_15_porcent}\nTotal: {salario_usuario + aumento}")