# Ejercicio 1 PILA
#E: numero entero 
#S: suma de sus dig
#S: no convierte a string ni lista

def sumar_digitos(numero):
    numero = abs(numero)
    #si el numero es un digito retorna ese
    if numero < 10:
        return numero
    #recursiva primero, luego se suma el dígito actual (ultimo digito)
    return sumar_digitos(numero // 10) + (numero % 10)


#prueba
print(sumar_digitos(1234)) #10
print(sumar_digitos(9001)) #10
print(sumar_digitos(7)) #7
print(sumar_digitos(0)) #0
