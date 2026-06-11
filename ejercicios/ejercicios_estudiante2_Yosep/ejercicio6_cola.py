# Ejercicio 6 COLA
#E: lista de numeros enteros
#S:cantidad de bloques de numeros consecutivos iguales
#R: sea una lista

def contar_bloques_iguales(lista, conteo=0):
    # Caso base: lista vacía
    if len(lista) == 0:
        return conteo
    # Caso base: un solo elemento es siempre un bloque
    if len(lista) == 1:
        return conteo + 1
    # Si el primer elemento es diferente al siguiente, termina un bloque
    if lista[0] != lista[1]:
        return contar_bloques_iguales(lista[1:], conteo + 1)
    # Si son iguales, seguir avanzando sin contar nuevo bloque
    return contar_bloques_iguales(lista[1:], conteo)


# Casos de prueba
print(contar_bloques_iguales([1, 1, 2, 2, 2, 3, 1, 1]))  # 4
print(contar_bloques_iguales([5, 5, 5, 5]))  # 1
print(contar_bloques_iguales([1, 2, 3, 4]))   # 4
print(contar_bloques_iguales([])) # 0
