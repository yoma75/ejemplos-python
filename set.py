# Coleccion desordenada y no tiene un indice

animales = {'Perro','Vaca','Raton','Tigre'}
print(type(animales)) # set
print('')

# Vaca esta en la coleccion de animales..?
print('Vaca' in animales) # True
print('Cabra' in animales) # False
print('')

# .add: adicionar elementos
animales.add('Tiburon')
print(animales)
print('')

# .remove: eliminar 1 elemento
animales.remove('Raton')
print(animales)
print('')

# .clear: elimina todos los elementos 
animales.clear()
print(animales) # set()





