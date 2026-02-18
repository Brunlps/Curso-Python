salario = float(input("Digite o salário para calcular o imposto: "))
# A base é uma variável de auxilio
# Onde quardaremos o salário para usar nas operações do programa
base = salario
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
    
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)

print(f"Salário: R${salario:6.2f} \nImposto a pagar: R${imposto:6.2f} ")