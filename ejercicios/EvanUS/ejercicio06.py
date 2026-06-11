# Contar bloques iguales:
#E: Lista
#S: La cantidad de bloques de listas con numeros iguales, sacado de manera recursiva de pila
#R: Lista de numeros enteros

def contar_bloques_iguales(lista,chequeo=0, isfirst=True):
    if lista == [] and not isfirst:
        return 1
    if lista == [] and isfirst:
        return 0
    elif isfirst:
        return contar_bloques_iguales(lista[1:], lista[0], False)
    elif lista[0] == chequeo:
        return contar_bloques_iguales(lista[1:], chequeo, False)
    else:
        return 1 + contar_bloques_iguales(lista[1:], lista[0], False)