def mayor_lista(lista, res=None, isfirst=True):
    if lista == [] and isfirst:
        return 'La lista no tenia elementos inicialmente.'
    elif lista == []:
        return res
    else:
        if isfirst:
            return mayor_lista(lista[1:], res=lista[0], isfirst=False)
        else:
            return mayor_lista(lista[1:], res=lista[0], isfirst=False) if lista[0] > res else mayor_lista(lista[1:], res, isfirst=False)