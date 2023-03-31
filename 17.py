def paraula_mes_llarga(llista):
    paraula_llarga = llista[0]
    for paraula in llista:
        if len(paraula) > len(paraula_llarga):
            paraula_llarga = paraula
    return paraula_llarga

if __name__ == "__main__":
    llista = []
    n = int(input("Ingrese la cantidad de palabras que quiere en la lista: "))
    for i in range(n):
        paraula = input(f"Ingrese la palabra {i+1}: ")
        llista.append(paraula)
    paraula_llarga = paraula_mes_llarga(llista)
    print(f"La palabra más larga de la lista {llista} es '{paraula_llarga}'")
