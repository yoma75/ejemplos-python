# Solicitar el nombre del alumno, la cantidad de calificaciones que se promediaran, calcular el promedio y si el promedio es mayor o igual a 70 aprobara de lo contrario sera reprobado. Al final debera preguntarle al usuario si desea capturar otro alumno, el programa debera repetirse mientras la respuesta sea diferente de "No"

respuesta = "si"
while (respuesta!="no"):
    nombre = input("Escribe el nombre del alumno:")
    notas = int(input("Cuantas calificaciones vas a promediar:"))

    suma = 0
    for i in range(1,notas+1):
        print("Ingresa la calificacion numero",i,":")
        calificaciones=input()
        calificaciones=float(calificaciones)
        suma = suma + calificaciones
    
    promedio = suma / notas

    # Comprobar si aprobo o reprobo
    if promedio >= 70:
        print("Felicitaciones", nombre,"has aprobado, tu promedio es de:", promedio)
    else:
        print("Lo siento", nombre,"has perdido, tu promedio es de:", promedio)
    
    # Desea seguir el usuario..?
    print("Desea ingresar otro alumno (si / no):")
    respuesta=input()


