# Pedir un numero entero al usuario e indicarsi es par

print("")
numero = int(input("Digita un numero: "))
print("")

if numero % 2 == 0:
    print("El numero",numero,"es par")
else:
    print("El numero",numero,"es impar")