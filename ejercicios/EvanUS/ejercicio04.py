def largo(numero):
    if numero < 10:
        return 1
    else:
        return 1 + largo(numero//10)

def invertir_numero(numero):
    if isinstance(numero, int) and numero >= 0:
        return invertir_numero_aux(numero, largo(numero) - 1)
    else:
        return 'Solo se admiten numeros enteros positivos o 0.'
    
def invertir_numero_aux(numero,exp):
    print(numero, exp)
    if numero == 0:
        return 0
    else:
        return ( (numero % 10) * (10 ** exp) ) + invertir_numero_aux(numero // 10, exp - 1)