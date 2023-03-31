def gran_llista(llista):
    maxim = llista[0]
    for num in llista:
        if num > maxim:
            maxim = num
    return maxim

if __name__ == "__main__":
    llista = []
    n = int(input("Ingrese la cantidad de números que quiere en la lista: "))
    for i in range(n):
        num = int(input(f"Ingrese el número {i+1}: "))
        llista.append(num)
    maxim = gran_llista(llista)
    print(f"El número més gran de la llista {llista} és {maxim}")
