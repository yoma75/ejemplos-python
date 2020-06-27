# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario y <n> es el número de letras que tienen el nombre.

nombre = input("Escribe tu nombre: ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")

