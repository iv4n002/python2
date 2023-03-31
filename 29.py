quantitat = float(input("Introdueixi la quantitat a sol·licitar (entre 50000€ i 800000€): "))
interes = float(input("Introdueixi l'interès (entre 0.5% i 13%): "))
anys = int(input("Introdueixi el nombre d'anys (entre 3 anys i 40 anys): "))

if quantitat < 50000 or quantitat > 800000:
    print("La quantitat introduïda no és vàlida.")
elif interes < 0.5 or interes > 13:
    print("El tipus d'interès introduït no és vàlid.")
elif anys <3 or anys >40:
        print ("El període ha de ser entre tres y quaranta anys")
else:
    Cfinal = round(quantitat * (1 + interes/100) ** anys,2)
    print(f"La quantitat final seria de {Cfinal}€")