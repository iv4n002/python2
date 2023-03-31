opcion = input("¿Quieres imprimir números pares o impares? ")
limite = int(input("Introduce el límite superior: "))

if opcion == "pares":
    i = 2
    while i <= limite:
        print(i)
        i += 2
elif opcion == "impares":
    i = 1
    while i <= limite:
        print(i)
        i += 2
else:
    print("Opción no válida.")
