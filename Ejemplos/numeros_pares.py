# Pedir dos numeros por teclado y mostrar todos los numeros pares comprendidos entre ambos

numero1 = int(input("Digite el primer numero: "))

# Forzar que este segundo numero sea mayor que el primero
numero2=numero1
while numero2 <= numero1:
    numero2 = int(input("Digite el segundo numero: "))

for n in range(numero1, numero2+1):
    if n % 2 == 0:
        print(n)