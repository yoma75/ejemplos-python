# pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años, y muestre por pantalla el capital obtenido en la inversión redondeado con dos decimales.
print("")
monto = float(input("Cantidad de dinero a invertir: $ "))
interes = float(input("Interes anual de: "))
years = int(input("A cuantos años lo desea: "))

print("Inversion total: "+str(round(monto * (interes / 100 + 1) ** years, 2)))