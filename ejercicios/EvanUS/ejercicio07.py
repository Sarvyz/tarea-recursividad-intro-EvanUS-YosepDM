# Separar por paridad:
#E: Numero
#S: Eliminar impares auxiliar del numero dado
#R: Solo numeros positivos enteros

def eliminar_impares(numero):
    if isinstance(numero, int) and numero >= 0:
        return eliminar_impares_aux(numero, 0)
    else:
        return 'Solo se admiten numeros enteros positivos o 0.'
    
# Separar por paridad auxiliar:
#E: Numero, exponente (dado por la funcion no auxiliar como 0)
#S: El numero sin los digitos impares o 0, realizado de manera recursiva de pila
#R: Numero entero positivo dado por la funcion no auxiliar

def eliminar_impares_aux(numero,exp):
    if numero == 0:
        return 0
    elif (numero % 10) % 2 == 0:
        return (numero % 10) * (10 ** exp) + eliminar_impares_aux(numero // 10, exp + 1)
    else:
        return eliminar_impares_aux(numero // 10, exp)