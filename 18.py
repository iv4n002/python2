def filtrar_paraules(llista, x):
    paraules_filtrades = []
    for paraula in llista:
        if len(paraula) > x:
            paraules_filtrades.append(paraula)
    return paraules_filtrades

if __name__ == "__main__":
    llista = []
    n = int(input("Ingrese la cantidad de palabras que quiere en la lista: "))
    for i in range(n):
        paraula = input(f"Ingrese la palabra {i+1}: ")
        llista.append(paraula)
    x = int(input("Ingrese el número mínimo de caracteres que desea para filtrar: "))
    paraules_filtrades = filtrar_paraules(llista, x)
    print(f"Las palabras de la lista {llista} que tienen más de {x} caracteres son: {paraules_filtrades}")
