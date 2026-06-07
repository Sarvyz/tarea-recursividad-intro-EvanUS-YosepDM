def sumar_digitos(numero):
    if isinstance(numero, int) and numero >= 0:
        return sumar_digitos_aux(numero)
    else:
        return 'Solo se admiten numeros enteros y positivos.'
    
def sumar_digitos_aux(numero,res=0):
    if numero == 0:
        return res
    else:
        res += numero % 10
        return sumar_digitos_aux((numero // 10), res)