# Exercício 8.4:
    # Escreva uma função que receba a base e a altura de truângulo 
    # e retorne sua área A = (base x altura / 2)
    
base = float(input("Digite o valor da Base do Triângulo: "))
altura = float(input("Digite o valor da Altura do Triângulo: "))

def area_triangulo(base, altura,):
    return (base * altura) / 2

area = area_triangulo(base, altura)

print(f"A área do triângulo: {area:.2f}")    