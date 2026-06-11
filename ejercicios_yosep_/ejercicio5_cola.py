# Ejercicio 5 COLA
#E:numero entero positivo 
#S: numero con los pares del original
#R: no convierte a string

def eliminar_impares(numero, acumulado=0, potencia=1):
    # Caso base: no quedan más dígitos
    if numero == 0:
        return acumulado
    ultimo = numero % 10
    # Si el dígito es par, agregarlo al acumulado
    if ultimo % 2 == 0:
        nuevo_acumulado = ultimo * potencia + acumulado
        nueva_potencia = potencia * 10
    else:
        nuevo_acumulado = acumulado
        nueva_potencia = potencia
    # Llamada de cola con el número sin el último dígito
    return eliminar_impares(numero // 10, nuevo_acumulado, nueva_potencia)


# Casos de prueba
print(eliminar_impares(123456)) # 246
print(eliminar_impares(97531)) # 0
print(eliminar_impares(80246)) # 80246
print(eliminar_impares(1007)) # 0
