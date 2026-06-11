# Ejercicio 10 PILA
#E:lista de numeros
#S: lista de pares
#R: no usar ciclos

def comprimir_repetidos(lista):
    #lista vacía
    if len(lista) == 0:
        return []
    #un solo elemento
    if len(lista) == 1:
        return [[lista[0], 1]]
    #recursiva 
    resto_comprimido = comprimir_repetidos(lista[1:])
    
    if resto_comprimido[0][0] == lista[0]:
        return [[lista[0], resto_comprimido[0][1] + 1]] + resto_comprimido[1:]
    # Si es diferente, agregar como nuevo bloque
    return [[lista[0], 1]] + resto_comprimido


#prueba
print(comprimir_repetidos([1, 1, 1, 2, 2, 3, 1, 1])) # [[1,3],[2,2],[3,1],[1,2]]
print(comprimir_repetidos([5, 5, 5, 5])) # [[5,4]]
print(comprimir_repetidos([1, 2, 3, 4])) # [[1,1],[2,1],[3,1],[4,1]]
print(comprimir_repetidos([])) # []
