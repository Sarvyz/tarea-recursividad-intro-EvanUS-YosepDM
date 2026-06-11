# Ejercicio 2 PILA
#E: numero entero
#S: cantidad de dígitos pares
#R: no convertir a string ni a lista

def contar_pares(numero):
    numero = abs(numero)
    if numero < 10:
        return 1 if numero % 2 == 0 else 0
    # Verificar el último dígito, luego llamada recursiva con el resto
    ultimo = numero % 10
    es_par = 1 if ultimo % 2 == 0 else 0
    return contar_pares(numero // 10) + es_par


#prueba
print(contar_pares(2486)) #4
print(contar_pares(13579))# 0
print(contar_pares(12040))#4
print(contar_pares(7)) #0
