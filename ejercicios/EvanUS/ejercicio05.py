# Eliminar impares:
#E: Numero
#S: Eliminar pares auxiliar del numero dado
#R: Solo numeros positivos enteros

def eliminar_impares(numero):
    if isinstance(numero, int) and numero >= 0:
        return eliminar_impares_aux(numero,)
    else:
        return 'Solo se admiten numeros enteros positivos o 0.'
    
#Invertir numero auxiliar:
#E: Numero, exponente (dado por largo(numero) - 1)
#S: El numero sin los digitos impares o 0, realizado de manera recursiva de pila
#R: Numero entero positivo dado por la funcion no auxiliar

def eliminar_impares_aux(numero,exp):
    if numero == 0:
        return 0