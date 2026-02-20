# ==== Programa 8.2 ====
# Como não escrever uma função
l = []
def soma(l):
    total = 0
    for x in range(5):
        total += l[x]
        x += 1
    return total
print(soma([1, 2, 45, 200, 50])) # 
# print(soma()) 
    