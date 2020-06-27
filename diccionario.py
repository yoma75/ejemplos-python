# Nos permite definir claves (keys) y valores, se utiliza para definir objetos de la vida real, son mutables: permite modificar los valores

producto = {
    "Nombre": "Libro",
    "Cantidad": 3,
    "Precio": 5400
}

persona = {
    "Nombre": "Ana",
    "Apellido": "Suarez",
    "Edad": 45
}

print(type(producto)) # dict

# Metodos y propiedades de los diccionarios
print(dir(producto))
print('')
print('----------------------------------------------------')

# keys: obtener solo las llaves
print(persona.keys()) # nombre, apellido, edad

# items: obtener solo los valores
print(persona.items()) # 





