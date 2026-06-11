# Ejercicio 8 PILA
#E: lista de numero
#S: lista
#R: usa lista

def detectar_valles(lista):
    if len(lista) < 3:
        return []
    
    valles = detectar_valles(lista[1:])
    # Al regresar, verificar si los primeros 3 forman un valle
    if lista[1] < lista[0] and lista[1] < lista[2]:
        return [[lista[0], lista[1], lista[2]]] + valles
    return valles


#prueba
print(detectar_valles([5, 1, 6, 3, 8, 2, 7]))  #[[5,1,6],[6,3,8],[8,2,7]]
print(detectar_valles([1, 2, 3, 4, 5])) # []
print(detectar_valles([9, 4, 8, 2, 6])) # [[9,4,8],[8,2,6]]
print(detectar_valles([3, 1])) # []
