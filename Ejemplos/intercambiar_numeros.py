# Pedir dos numeros por teclado, si el primer numero es mayor que el segundo, intercambiarlos

aux = 0
a = int(input("Digita el primer numero: "))
b = int(input("Digita el segundo numero: "))
print("") 

print("El primer numero es: ",a, "y el segundo numero es: ",b)
if a > b:
    aux = a
    a = b
    b = aux
print("El primer numero es: ",a, "y el segundo numero es: ",b)

