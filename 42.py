def hi_ha_duplicats(llista):
    return len(llista) != len(set(llista))

# Programa principal
llista = input("Introdueix una llista de nombres separats per espais: ").split()
if hi_ha_duplicats(llista):
    print("Hi ha elements duplicats a la llista.")
else:
    print("No hi ha elements duplicats a la llista.")
