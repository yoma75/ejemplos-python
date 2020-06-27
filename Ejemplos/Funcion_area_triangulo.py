# Realizar una funcion que imprima "Hola mundo"

# def area_triangulo(base, altura):
#     return(base*altura)/2
   
print("------------------------------------------------------------")
# print("El area del triangulo es de:",area_triangulo(5,7),"cms")

# triangulo1 = area_triangulo(5,7)
# triangulo2 = area_triangulo(9,6)  

# print("El area del triangulo es de:",triangulo1,"cms")
# print("El area del triangulo es de:",triangulo2,"cms")


# Nombre de la variable
# lambda: palabra reservada
# Parametros: base y altura
# Dos puntos ":" hace de return
# Calculos de la funcion
area_triangulo = lambda base, altura: (base * altura)/2

base=int(input("Digite la base: "))
altura=int(input("Digite la altura: "))

print("El area del triangulo es de:",area_triangulo(base, altura),"cms")

