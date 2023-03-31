import random
llista=[]
def hi_ha_duplicats(llista):
    return len(llista) != len(set(llista))

# Programa principal

if hi_ha_duplicats(llista):
    print("Hi ha elements duplicats a la llista.")
else:
    print("No hi ha elements duplicats a la llista.")


def llista_20_elements():

    for _ in range(20):
        llista.append(random.randint(1, 100))
    return llista

# Programa principal
llista = llista_20_elements()
print("Llista generada aleatòriament: ", llista)

if hi_ha_duplicats(llista):
    print("Hi ha elements duplicats a la llista.")
else:
    print("No hi ha elements duplicats a la llista.")
