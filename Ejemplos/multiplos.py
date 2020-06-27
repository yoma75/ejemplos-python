# Pedir dos numeros al usuario e indicar si el primero es multiplo del segundo. En caso contrario, comprobar si el segundo es multiplo del primero:

numero1 = int(input("Digita el primer numero: "))
numero2 = int(input("Digita el segundo numero: "))
print("")

if numero1 % numero2 == 0:
    print(numero1, "es multiplo de ",numero2)
elif numero2 % numero1 == 0:
    print(numero2, "es multiplo de ", numero1)
else:
    print("No son multiplos")

