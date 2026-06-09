#E: Lista
#S: Lista con secuencias de 3 elementos consecutivos en el que el elemento central sea menor que el anterior y posterior
#R: Lista de solo enteros positivos

def detectar_valles(lista, res = []):
    if len(lista) < 3:
        return res
    elif lista[0] > lista[1] < lista[2]:
        return detectar_valles(lista[1:], res + [[lista[0], lista[1], lista[2]]])
    else:
        return detectar_valles(lista[1:], res)