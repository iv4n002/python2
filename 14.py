def crear_punts(llista):
    for num in llista:
        print("." * num + "\n")

if __name__ == "__main__":
    llista = input("Introdueix una llista de números separats per comes: ")
    llista = [int(num) for num in llista.split(",")]
    crear_punts(llista)
