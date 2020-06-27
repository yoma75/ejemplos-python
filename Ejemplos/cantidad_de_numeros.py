# Pedir numeros al usuario hasta que introduzca uno negativo. Al finalizar mostrar la cantidad de numeros introducidos sin contar el negativo: 

numero = 0
contador = 0
while numero >= 0:
    numero = int(input("Introduce el numero: "))   
    if numero >= 0:
        contador = contador + 1

# contador = contador -1
print("Se ha introducido ",contador, " numeros")