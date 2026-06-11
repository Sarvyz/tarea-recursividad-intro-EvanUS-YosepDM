# Ejercicio 4 COLA
#E: numero entero
#S: el número con sus dígitos en orden inverso
#R: no convertir a string ni a lista

def invertir_numero(numero, acumulado =0):
    acumulado = 0
    # Caso base: no quedan más dígitos
    if numero == 0:
        return acumulado
    ultimo = numero % 10
    # Desplazar el acumulado una posición y agregar el dígito actual
    nuevo_acumulado = acumulado * 10 + ultimo
    # Llamada de cola: avanzar sin el último dígito
    return invertir_numero(numero // 10, nuevo_acumulado)


# Casos de prueba
print(invertir_numero(1234))  # 4321
print(invertir_numero(900))   # 9
print(invertir_numero(5071))  # 1705
print(invertir_numero(8))     # 8
