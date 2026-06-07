# Sumar digitos:
#E: Numero
#S: Sumar digitos auxiliar del numero dado
#R: Numero entero positivo

def sumar_digitos(numero):
    if isinstance(numero, int) and numero >= 0:
        return sumar_digitos_aux(numero)
    else:
        return 'Solo se admiten numeros enteros y positivos.'

# Sumar digitos auxiliar:
#E: Numero, res (establecido inicialmente en 0)
#S: Suma de los digitos de manera recursiva de cola
#R: Numero entero positivo dado por la funcion no auxiliar

def sumar_digitos_aux(numero,res=0):
    if numero == 0:
        return res
    else:
        res += numero % 10
        return sumar_digitos_aux((numero // 10), res)