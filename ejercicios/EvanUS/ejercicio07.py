# Separar por paridad:
#E: Numero
#S: Lista con un numero hecho con solo los numeros pares y otro numero hecho con solo los impares, realizado de manera recursiva de pila
#R: Numero entero positivo

def separar_por_paridad(numero):
    if numero == 0:
        return [0,0]
    digito = numero % 10
    pares = separar_por_paridad(numero // 10)
    impares = separar_por_paridad(numero // 10)
    if digito % 2 == 0:
        pares = pares * 10 + digito
    else:
        impares = impares * 10 + digito
    return [pares, impares]