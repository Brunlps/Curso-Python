   
init = int(input('Digite um número: '))
somaPar = 0
for numberPar in range(1, init):
    
    if numberPar % 2 == 0:
        
        print(f'Os numeros pares são: {numberPar}')
        
    somaPar +=numberPar
print(f'Todos os números pares somados:{somaPar} ')
          