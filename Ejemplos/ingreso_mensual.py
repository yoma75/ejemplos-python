# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

print("")
edad = int(input("Digita tu edad: "))
sueldo = int(input("Digita tus ingresos mensuales: $ "))

if(edad > 16 and sueldo >= 950000):
    print("Tu edad es de "+str(edad)+" años y tu sueldo mensual es de: $ "+str(sueldo))
    print("*** Debes de Tributar ***")
else:
    print("___ NO debes de Tributar ___")