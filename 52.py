def es_primer(num):
    """
    Función que verifica si un número es primo o no.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def nombres_primers():
    """
    Función que muestra los números primos entre 1 y 100 y devuelve su cantidad.
    """
    primers = []
    for i in range(1, 101):
        if es_primer(i):
            primers.append(i)
            print(i, end=" ")
    print()
    return len(primers)

print("Selecciona una opción:")
print("1. Mostrar números primos entre 1 y 100 y contarlos")
print("2. Salir")

opcion = int(input())

if opcion == 1:
    print("Los números primos son:")
    cantidad = nombres_primers()
    print("Hay", cantidad, "números primos entre 1 y 100")
elif opcion == 2:
    print("Adiós!")
else:
    print("Opción inválida.")
