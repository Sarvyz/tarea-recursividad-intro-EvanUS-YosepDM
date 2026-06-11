# Sublistas ascendentes:
#E: Lista
#S: Sublistas ascendentes auxiliar de la lista dada
#R: Lista de numeros enteros

def sublistas_ascendentes(lista):
    if lista == []:
        return []
    res = sublistas_ascendentes_aux(lista)
    return [res[0]] + sublistas_ascendentes(res[1])

# Sublistas ascendentes auxiliar:
#E: Lista, anterior (dado por defecto como -1)
#S: La sublista ascendente actual y donde continua la lista, realizado de manera recursiva de pila
#R: Lista de numeros enteros dada por la funcion no auxiliar

def sublistas_ascendentes_aux(lista, anterior=-1):
    if lista == [] or lista[0] <= anterior:
        return [[], lista]
    else:
        res = sublistas_ascendentes_aux(lista[1:], lista[0])
        return [[lista[0]] + res[0], res[1]]