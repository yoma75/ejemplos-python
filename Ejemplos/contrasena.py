#  preguntar al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

clave = 'entrada'
password = input("Escriba la contraseña de ingreso: ")

if clave == password.lower():
    print("Contraseña correcta")
else:
    print("Contraseña INCORRECTA")

