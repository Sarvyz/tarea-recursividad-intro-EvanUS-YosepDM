# Largo:
#E: Numero
#S: Cantidad de digitos, sacado de manera recursiva de pila
#R: Numero entero, positivo

def largo(numero):
    if numero < 10:
        return 1
    else:
        return 1 + largo(numero//10)

# Invertir numero:
#E: Numero
#S: Invertir numero auxiliar del numero dado
#R: Solo numeros positivos enteros

def invertir_numero(numero):
    if isinstance(numero, int) and numero >= 0:
        return invertir_numero_aux(numero, largo(numero) - 1)
    else:
        return 'Solo se admiten numeros enteros positivos o 0.'
    
#Invertir numero auxiliar:
#E: Numero, exponente (dado por largo(numero) - 1)
#S: El numero con sus digitos invertidos, realizado de manera recursiva de pila
#R: Numero entero positivo dado por la funcion no auxiliar

def invertir_numero_aux(numero,exp):
    if numero == 0:
        return 0
    else:
        return ( (numero % 10) * (10 ** exp) ) + invertir_numero_aux(numero // 10, exp - 1)