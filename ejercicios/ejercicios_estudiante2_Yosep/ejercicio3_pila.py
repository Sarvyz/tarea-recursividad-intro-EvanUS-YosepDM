# Ejercicio 3 PILA
#E: lista de numeros
#S: el numero mas grande de la lista
#R: no usar max

def mayor_lista(lista):
    #lista con un solo elemento
    if len(lista) == 1:
        return lista[0]
    mayor = mayor_lista(lista[1:])
    #comparar con el primer elemento
    if lista[0] > mayor:
        return lista[0]
    return mayor


#prueba
print(mayor_lista([4, 8, 1, 9, 3])) #9
print(mayor_lista([10, 2, 5, 7])) #10
print(mayor_lista([-3, -8, -1, -10])) # -1
print(mayor_lista([6])) #6
