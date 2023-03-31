def crear_llista_fitxer(nom_fitxer):
    with open(nom_fitxer, 'r') as fitxer:
        contingut = fitxer.read()
        llista = contingut.split()
        return llista

# Ejemplo de uso
nom_fitxer = input("Introduce el nombre del archivo: ")
llista = crear_llista_fitxer(nom_fitxer)
print("Lista creada a partir del archivo:", llista)
