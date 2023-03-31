def index_paraula(llista, paraula):
    low = 0
    high = len(llista) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = llista[mid]

        if guess == paraula:
            return mid
        elif guess > paraula:
            high = mid - 1
        else:
            low = mid + 1

    return -1


# Programa principal
llista = []

while True:
    paraula = input("Introduce una palabra (o 'exit' para terminar): ")
    if paraula == "exit":
        break
    llista.append(paraula)

llista.sort()

paraula = input("Introduce la palabra a buscar: ")
index = index_paraula(llista, paraula)

if index == -1:
    print("La palabra no se encuentra en la lista.")
else:
    print("La palabra", paraula, "se encuentra en la posición", index, "de la lista.")
