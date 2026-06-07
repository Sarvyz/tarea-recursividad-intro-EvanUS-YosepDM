def contar_pares(numero):
    if isinstance(numero, int) and numero >= 0:
        return contar_pares_aux(numero)
    else:
        return 'Solo se admiten numeros enteros y positivos.'
    
def contar_pares_aux(numero, isfirst = True, res=0):
    if numero == 0 and isfirst:
        return 1
    elif numero == 0:
        return res
    else:
        if (numero % 10) % 2 == 0:
            res += 1
        return contar_pares_aux(numero//10,False,res)
    
print(contar_pares(2486))
print(contar_pares(13579))
print(contar_pares(12040))
print(contar_pares(7))