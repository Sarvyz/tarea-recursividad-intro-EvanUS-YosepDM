#E: Lista
#S: Lista de sublistas, sublistas con [elemento, # de apariciones]
#R: Lista de numeros enteros

def comprimir_repetidos(lista, n=0, apariciones=0, res=[],isfirst = True):
    if lista == [] and not isfirst:
        return res + [[n,apariciones]]
    elif lista == [] and isfirst:
        return res
    elif isfirst:
        return comprimir_repetidos(lista[1:],lista[0],1,res,False)
    elif lista[0] == n:
        return comprimir_repetidos(lista[1:], n, apariciones+1,res,False)
    else:
        return comprimir_repetidos(lista[1:], lista[0], 1, res + [[n, apariciones]],False)