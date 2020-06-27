# Listas: sirve para almacenar colecciones de datos son mutables osea se pueden modificar despues de creadas

# Imprime directorio a utilizar en las listas
# print(dir(dias)) dias: es una lista

demo_list = [1, 'hello', 1.54, True, [1,2,3]]
colores = ['amarillo', 'azul', 'verde']
print("")
print(type(demo_list))

numeros = list((1,2,3,4,5))
print(numeros)
print('-------------------- ')

# range: Rango de donde a donde
# Crear una lista en este range (numero de inicio, hasta donde + 1 de mas) y guardelo en la variable numeritos, en este caso imprime la lista de 1 a 100
numeritos = list(range(1, 101))
print(numeritos)

# Que metodos puedo usar en list
# print(dir(colores))

print('-------------------- ')

# len: longitud
print(len(colores)) # 3
print(len(demo_list)) # 5
print('-------------------- ')

print(colores[1]) # azul

# Amarillo esta en colores..?
print('amarillo' in colores) # True
print(' ')
print('--------------------------------------------------------------------------------------- ')
print('')


# colores = ['amarillo', 'azul', 'verde']
# En el indice [1] esta 'azul' cambielo por 'rojo'
print('Colores originales:',colores)
colores[1] = 'rojo'
print('Cambio de color en el indice [1]:',colores) # ['amarillo', 'rojo', 'verde']
print(' ')
print('--------------------------------------------------------------------------------------- ')
print('')

# A la lista de colores quiero agregar (append) un nuevo elemento llamado violeta
# Si quiero pasar varios elementos debo convertirlos en una TUPLA ()
colores.append('violeta')
print('Con append:',colores)
print(' ')

# colores.append(('marron', 'blanco', 'plateado'))
print(colores) # ['amarillo', 'rojo', 'verde' 'violeta', ('marron', 'blanco', 'plateado')]
print(' ')
print('------------------------------------------------------------------------------------------------- ')
print('')

# Para que me salga la anterior lista sin los parentesis ( ) se debe usar EXTEND
colores.extend(('marron', 'blanco', 'plateado'))
print('Con extend:',colores) # ['amarillo', 'rojo', 'verde' 'violeta','marron', 'blanco', 'plateado']
print(' ')
print('------------------------------------------------------------------------------------------------- ')
print('')

# Insertar un elemento en una posicion dada, en la posicion 2 inserte (insert) 'rosado'
colores.insert(2, 'rosado')
print('Con insert:',colores) # ['amarillo', 'rojo', 'rosado', 'verde' 'violeta','marron', 'blanco', 'plateado']
print(' ')
print('------------------------------------------------------------------------------------------------- ')
print('')

# Eliminar (pop) un elemento de la lista 
colores.pop() # Elimina el ultimo sino se le da el indice, osea el plateado
print('Con pop:',colores)
colores.pop(1) # Elimina el indice 1
print('Con pop 1:',colores)

# Remover (remove) un elemento en especifico
colores.remove('marron')
print('Con remove:',colores)

# clear (limpia) toda la lista
# colores.clear()
# print('Con clear:',colores)
print(' ')
print('------------------------------------------------------------------------------------------------- ')
print('')

# longitud de la lista colores
print(len(colores)) # 5
print(' ')
print('------------------------------------------------------------------------------------------------- ')
print('')

# Ordenar alfabeticamente de la A-Z
colores.sort()
print('Ordenados de la A-Z:',colores) 

# Ordenar alfabeticamente de la Z-A
colores.sort(reverse=True)
print('Ordenados de la Z-A:',colores)
print(' ')
print('------------------------------------------------------------------------------------------------- ')
print('')

# imprimir un determinado indice (index) de color de la lista
print(colores.index('blanco')) # 3
print(' ')
print('------------------------------------------------------------------------------------------------- ')
print('')

# Contar (count) cuantas veces esta repetido un determinado elemento
print(colores.count('rosado')) # 1
print(' ')
print('------------------------------------------------------------------------------------------------- ')
print('')

# Imprime apartir del indice 2 hasta el ultimo
animalitos=['Perro', 'Vaca', 'Leon', 'Loro', 'Delfin']
print(animalitos[2:]) # Leon, Loro, Delfin

# Imprime apartir del indice 2 hacia el inicio
print(animalitos[:2]) # Perro, Vaca
print('------------------------------------------------------------------------------------------------- ')
print('')

# Recorrer la lista con for
dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for indice in range(0,7):
    print(dias[indice])
print('')

# Cambia el indice 0, que es Monday por Lunes y Sunday por Domingo:
dias[0]='Lunes'
dias[6]='Domingo'
for indice in range(0,7):
    print(dias[indice])
print('')

# Lista vacia y se agrega (append: inserta siempre al final) un elemento
paises=[]
paises.append('Colombia')
print(paises) # ['Colombia']

paises.append('Uruguay')
print(paises) # ['Colombia', 'Uruguay']
print('')

# Count: contar cuantas veces aparece un dato dentro de la lista
print(paises.count('Uruguay')) # 1
print(paises.count('Roma')) # 0
print('-----------------------------------------------------------------------------')

# Extend: extender la lista con datos de otra lista
ciudades=['Bogota', 'Montevideo']
print(ciudades)

# pego la lista de paises con la lista de ciudades
paises.extend(ciudades)
print(paises) # ['Colombia', 'Uruguay', 'Bogota', 'Montevideo']


# Index: me devuelve la posicion del dato dentro de la lista y si el dato no esta devuelve un error
print("")
print("Bogota esta en el indice numero: ", paises.index('Bogota')) # 2
print("-------------------------------------------------------------------------")


# Insert: insertar un dato en una posicion diferente a la ultima (append)
paises.insert(1,'Brasil')
print(paises) # ['Colombia', 'Brasil', 'Uruguay', 'Bogota', 'Montevideo']
print("")

# Pop: devuelve el ultimo elemento de la lista pero lo ELIMINA
# Pop(posicion): devuelve la posicion del elemento de la lista pero lo ELIMINA
paises.pop()
print(paises) # ['Colombia', 'Brasil', 'Uruguay', 'Bogota'], elimino el ultimo que era 'Montevideo'

paises.pop(2)
print(paises) # ['Colombia', 'Brasil', 'Bogota'], elimino la posicion 2 que era 'Uruguay'


# Remove: borra el contenido de la lista
paises.remove('Brasil')
print(paises) # ['Colombia', 'Bogota']


# Reverse: lista en reversa los elementos
paises.reverse()
print(paises) # ['Bogota', 'Colombia']
print("")


#  Sort: ordena la lista de menor a mayor
colores.sort()
print(colores) # ['amarillo', 'blanco', 'rosado', 'verde', 'violeta']


# Para ordenarlo de mayor a menor se aplica reverse
colores.reverse()
print(colores) # ['violeta', 'verde', 'rosado', 'blanco', 'amarillo']


# Clear: limpia la lista, la deja sin elementos
colores.clear()
print(colores)


