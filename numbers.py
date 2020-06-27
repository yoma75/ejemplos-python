# type: que tipo de variable es
print(type(98)) # int
print(type(43.4)) # float 
print(type("Hola"))
print("--------------------------------------------")

# ** : al cubo
print('2 al cubo es: ' ,2 ** 3) # 8, 2*2=4*2=8

# % : muestra el residuo de una division
print('El residuo de la division 3 % 2 es: ' ,3 % 2)

# / : division con resultado tipo float
print('La division entre 3 / 2 es:' ,3 / 2, 'resultado tipo float') # 1.5

# // : division con resultado tipo entero
print('La division entre 3 // 2 es:' ,3 // 2, 'resultado tipo entero') # 1
print(' ')

# input: permite pedir datos por teclado
edad = input('Digita tu edad: ')
print(edad +' años') # edad años

# Se coloca int para pasar la variable edad a tipo entero porque es de tipo string, se guarda en otra variable
nueva_edad = int(edad) + 5
print('Mas 5 años es:',nueva_edad,'años')
print("-------------------------------------------")

# Elige el mayor numero
print(max(43,56,76,98,126)) # 126

# Elige el menor numero
print(min(43,65,87,3)) # 3







