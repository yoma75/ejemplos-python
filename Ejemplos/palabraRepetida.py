# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

print("")
nombre = input("Cual es su nombre: ")
numero = int(input("Cuantas veces quiere repetir su nombre: "))

print((nombre + "\n") * numero)

