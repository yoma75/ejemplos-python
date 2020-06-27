myVariable = "hola mundo"

# dir: Muestra por consola las funciones para usar y alterar la variable
# print(dir(myVariable))

# Estas funciones solo se pueden aplicar para variables de tipo STRING
# upper: convierte el contenido de la variable en MAYUSCULAS
print(myVariable.upper()) # HOLA MUNDO

# lower: convierte el contenido de la variable en minusculas
print(myVariable.lower()) # hola mundo

# title: inicia en mayuscula cada una de las palabras de la variable
print(myVariable.title()) # Hola Mundo

# capitalize: primera letra en mayuscula de la variable
print(myVariable.capitalize()) # Hola mundo

# replace: reemplaza una palabra por otra (hola por Mi)
print(myVariable.replace('hola', 'Mi').upper()) # Mi mundo y lo convierte en MAYUSCULA

# count: cuenta cuantas veces esta repetido dicho caracter em mi variable
print(myVariable.count('o')) # 2 veces la letra O
print(myVariable.count(' ')) # 1 caracter vacio, osea el espacio entre las dos palabras: hola mundo

# startswith: quiero saber si la variable empieza con la palabra hello
print(myVariable.startswith('hello')) # False

# endswith: quiero saber si mi texto que esta en la variable termina en 'mundo'
print(myVariable.endswith('mundo')) # True

# split: separa el texto de la variable apartir del espacio, tambien se le puede decir por alguna letra o caracter
print(myVariable.split()) # ['hola', 'mundo']

# find: me dice en que posicion (indice) se encuentra un determinado caracter en este caso la letra 'a' de la palabra: hola
print(myVariable.find('a')) # 3
print(myVariable.find(' ')) # en que indice esta el espacio en blanco = '4' Hola mundo

# len: longitud de la variable
print(len(myVariable)) # 10 

# index: cual es el indice de una determinada letra
print(myVariable.index('m')) # hola mundo la letra 'm' esta en el indice = 5

# isnumeric: es numerico la variable
print(myVariable.isnumeric()) # False

# isalpha: es alfanumerico la variable
print(myVariable.isalpha()) # False

# Que caracter existe en el indice numero 6 de la variable 
print(myVariable[6]) # u 

# Que caracter existe de manera inversa en el indice numero -2 de la variable 
print(myVariable[-2]) # d, "hola mundo"


print('Noviembre 11 / 2019: ' +myVariable)

# len: cuenta los caracteres de la variable tipo string
print(len(myVariable)) # 10


cadena1 = "Michin "
cadena2 = "volando"
print(cadena1 * 5) # 5 veces Michin

cadena3 = cadena1 + cadena2
print(cadena3) # Michin volando

# Recorrer la cadena1 caracter por caracter
for indice in cadena3:
    print(indice) 

# [start:end:steps], imprime la cadena3 desde el indice 0 hasta el indice 13, haciendolo de 2 en 2
# M i c h i n     V o l  a  n  d  o
# 0 1 2 3 4 5  6  7 8 9 10 11 12 13
print(cadena3[0:13:2]) # Mci oad
print(cadena3[::2]) # Mci oad, tambien se puede escribir asi porque empieza en el indice 0 y va hasta el indice 13 de 2 en 2

# Imprime apartir del indice 3 hasta el indice 14
print(cadena3[3:14]) # hin volando



