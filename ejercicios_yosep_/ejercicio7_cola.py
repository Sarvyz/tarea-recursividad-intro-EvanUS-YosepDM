# Ejercicio 7 COLA
#E: entero positivo
#S: lista
#R: no convertir string ni lista

def separar_por_paridad(numero, pares=0, impares=0, pot_par=1, pot_impar=1):
    # Caso base: no quedan dígitos
    if numero == 0:
        return [pares, impares]
    ultimo = numero % 10
    if ultimo % 2 == 0:
        nuevo_pares = ultimo * pot_par + pares
        nueva_pot_par = pot_par * 10
        return separar_por_paridad(numero // 10, nuevo_pares, impares, nueva_pot_par, pot_impar)
    else:
        nuevo_impares = ultimo * pot_impar + impares
        nueva_pot_impar = pot_impar * 10
        return separar_por_paridad(numero // 10, pares, nuevo_impares, pot_par, nueva_pot_impar)


#prueba
print(separar_por_paridad(123456))  # [246, 135]
print(separar_por_paridad(80231))   # [802, 31]
print(separar_por_paridad(97531))   # [0, 97531]
print(separar_por_paridad(2468))    # [2468, 0]
