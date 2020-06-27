# def nombre_funcion():
#     * Instrucciones de la Funcion 
#     * return(opcional)

# def nombre_funcion(parametros):
#     * Instrucciones de la Funcion 
#     * return(opcional)

def saludo(nombre):
    print('Hello '+nombre)

saludo("Fredy")
print('--------------------------------')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def suma(num1, num2):
    return num1 + num2

print(suma(34,65))
print(suma(466,553))
print('')


# Funciones tipo lambda
# Nombre de la variable
# lambda: palabra reservada
# Parametros: numero1 y numero2
# Dos puntos ":" hace de return
# Calculos de la funcion
multiplicar = lambda numero1, numero2: numero1 * numero2
print(multiplicar(34,6))
print(multiplicar(4,5))



