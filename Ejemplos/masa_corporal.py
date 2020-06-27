# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

print("")
peso = input("Digita tu peso corporal: ")
estatura = input("Digita tu estatura: ")

# round: redondea el resultado, 2,2: dos decimales despues de la coma ,
imc = round(float(peso)/float(estatura)**2,2)

print("Tu indice de masa corporal es de: " +str(imc))

