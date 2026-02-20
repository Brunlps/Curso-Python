def pesquise(lista, valor):
    """ Essa função percorre a lista enumerando as posições.
    FOR passa pela lista procurando número questamos procurando.
    """
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return None
    
l = [10, 15, 20, 25, 30, 35, 40]
strings = [str(n) for n in l]
print(strings)
print(pesquise(l,25))
print(pesquise(l,80))
