# Pedir tres numeros y decir cual es el mayor

a = int(input("Digite el primer numero: "))
b = int(input("Digite el segundo numero: "))
c = int(input("Digite el tercer numero: "))
print("")

if a >= b and a >=c:
    print("El primer numero:",a, "es el mayor")
elif b >= a and b >= c:
    print("El segundo numero:",b, "es el mayor")
else:
    print("El tercer numero:",c, "es el mayor")
   

