def mayor_lista(lista, res = 0, isfirst=True):
    if lista == [] and isfirst:
        return 'La lista no tenia elementos inicialmente.'
    elif lista == []:
        return res
    else:
        return mayor_lista(lista[1:], res=lista[0], isfirst=False) if lista[0] > res else mayor_lista(lista[1:], res, isfirst=False)
    
print(mayor_lista([4, 8, 1, 9, 3]))
print(mayor_lista([10, 2, 5, 7]))
print(mayor_lista([-3, -8, -1, -10]))
print(mayor_lista([6]))