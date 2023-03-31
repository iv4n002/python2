def crear_repetits(num, caracter):
    return caracter * num

if __name__ == "__main__":
    num = int(input("Introdueix un número enter: "))
    caracter = input("Introdueix un caràcter: ")
    resultat = crear_repetits(num, caracter)
    print(resultat)
