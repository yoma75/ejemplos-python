# Entrar un numero y decir si esta entre el rango 0 al 10

numerica = int(input("Digita un numero entre el rango 0 al 10: "))
print("")

if numerica in range(0,10):
    print("El numero digitado SI ESTA en el rango")
    print("")
elif numerica in range(11,20):
    print("El numero esta entre el rango del 11 al 20")
elif numerica in range(21,30):
    print("El numero esta entre el rango del 21 al 30")
else:
    print("El numero digitado NO ESTA en el rango")
    print("")
