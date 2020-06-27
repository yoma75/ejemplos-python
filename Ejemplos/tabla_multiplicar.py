# Pedir un numero por teclado y mostrar su tabla de multiplicar hasta 10

print("")
numerito = int(input("Digite el numero de la tabla: "))
for n in range(1, 11):     
    print(numerito, "x",n, "=",(numerito * n ))
