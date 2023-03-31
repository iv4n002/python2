paraula1 = input("Introduïu la primera paraula: ")
paraula2 = input("Introduïu la segona paraula: ")

if len(paraula1) >= 3 and len(paraula2) >= 3:
    if paraula1[-3:] == paraula2[-3:]:
        print("Les dues paraules rimen!")
    elif paraula1[-2:] == paraula2[-2:]:
        print("Les dues paraules rimin un poc.")
    else:
        print("Les dues paruaules no rimen.")
else:
    print("Per verificar si les palabras riman cal que tinguin almenys tres lletres cada una. Si us plau, proveeu d'altres.") 