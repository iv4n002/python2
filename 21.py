def calcular_edad(any_actual, any_naixement):
    return any_actual - any_naixement

if __name__ == '__main__':
    any_actual = int(input("Introdueix l'any actual: "))
    noms = []
    naixements = []
    edats = []

    for i in range(4):
        nom = input("Introdueix el nom de la persona: ")
        naixement = int(input("Introdueix l'any de naixement de la persona: "))
        edat = calcular_edad(any_actual, naixement)
        noms.append(nom)
        naixements.append(naixement)
        edats.append(edat)

    print("\nNom\tData naixement\tAnys que farà aquest any")
    for i in range(4):
        print(f"{noms[i]}\t{naixements[i]}\t\t{edats[i]}")
