# For: permite recorrer cada uno de los elementos
frutas = ['banano', 'pera', 'uvas', 'melocoton']
for fruticas in frutas:
    if fruticas == "uvas":
        break # banano, pera, porque se cumple la condicion de arriba y deja de imprimir el resto de elementos
    print(fruticas)
    print('--------------------------------------------------')


frutas = ['banano', 'pera', 'uvas', 'melocoton']
for fruticas in frutas:
    if fruticas == "uvas":
        continue # Rompe la continuidad del bucle y sigue, de acuerdo a la condicion anterior, como encuentra uvas continua e imprime: banano, pera, melocoton
    print(fruticas)
    print('________________________________________')


# Recorre los numeros de 1 a 7
for numeros in range(1,8):
    print(numeros)
    print('________________________________________')

# Recorre el string 'python'
for letra in "python":
    print(letra)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')

# Pedir 10 numeros por teclado
for n in range(0,10):
    numero = int(input("Introduce un numero:"))

# ****************************************************************************
# Condicion while

numerito = 4

while numerito <=10:
    print(numerito)
    numerito = numerito + 1

