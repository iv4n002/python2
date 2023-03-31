def crear_punts(llista):
    for num in llista:
        print("." * num + "\n")

def dibuixar_imatge():
    llista = [2, 4, 6, 8, 6, 4, 2]
    for num in llista:
        crear_punts([num])

if __name__ == "__main__":
    dibuixar_imatge()
