# Hallar el cubo de un numero

# Nombre de la variable
# lambda: palabra reservada
# Parametros: numero
# Dos puntos ":" hace de return
# Calculos de la funcion
cubo = lambda numero: numero**3

print(cubo(3))


print("****************************************")

# El numero es par o impar
def espar(number):
    if number % 2 == 0:
        print("El numero",number,"es par")
    else:
        print("el numero",number,"es impar")    
    

print(espar(4345))
print(espar(260))
