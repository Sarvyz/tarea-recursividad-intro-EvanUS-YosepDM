# Ejercicio 9 COLA
#E: lista de numeros enteros
#S: lista de sublistas
#R: ninguna adicional 

def sublistas_ascendentes(lista, sublista_actual=None, resultado=None):
    # Inicializar parámetros en la primera llamada
    if sublista_actual is None:
        sublista_actual = []
    if resultado is None:
        resultado = []

    # Caso base: lista vacía
    if len(lista) == 0:
        if len(sublista_actual) > 0:
            return resultado + [sublista_actual]
        return resultado

    elemento = lista[0]

    # Si la sublista actual está vacía o el elemento sigue la secuencia ascendente
    if len(sublista_actual) == 0 or elemento > sublista_actual[-1]:
        return sublistas_ascendentes(lista[1:], sublista_actual + [elemento], resultado)

    # Si no es ascendente, cerrar la sublista actual e iniciar una nueva
    return sublistas_ascendentes(lista[1:], [elemento], resultado + [sublista_actual])


# Casos de prueba
print(sublistas_ascendentes([1, 2, 3, 1, 4, 5, 2]))  # [[1,2,3],[1,4,5],[2]]
print(sublistas_ascendentes([5, 4, 3, 2]))            # [[5],[4],[3],[2]]
print(sublistas_ascendentes([1, 3, 5, 7]))            # [[1,3,5,7]]
print(sublistas_ascendentes([2, 2, 3, 1, 2]))         # [[2],[2,3],[1,2]]
print(sublistas_ascendentes([]))                      # []
