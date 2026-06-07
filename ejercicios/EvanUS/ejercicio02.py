# Contar pares:
#E: Numero
#S: Contar pares auxiliar del numero dado
#R: Numero entero positivo

def contar_pares(numero):
    if isinstance(numero, int) and numero >= 0:
        return contar_pares_aux(numero)
    else:
        return 'Solo se admiten numeros enteros y positivos.'

# Contar pares auxiliar:
#E: Numero, isfirst (establecido inicialmente en True), res (establecido inicialmente en 0)
#S: Cantidad de digitos pares en el numero, contadas de manera recursiva de cola
#R: Numero entero positivo dado por la funcion no auxiliar

def contar_pares_aux(numero, isfirst = True, res=0):
    if numero == 0 and isfirst:
        return 1
    elif numero == 0:
        return res
    else:
        if (numero % 10) % 2 == 0:
            res += 1
        return contar_pares_aux(numero//10,False,res)