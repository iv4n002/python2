def comptar_vocals(paraula):
    vocals = ['a', 'e', 'i', 'o', 'u'] # llista de les vocals
    aparicions = [0, 0, 0, 0, 0] # per emmagatzemar el nombre d'aparicions de cada vocal
    
    for lletra in paraula:
        if lletra.lower() in vocals: # convertim la lletra a minúscules i comprovem si és una vocal
            aparicions[vocals.index(lletra.lower())] += 1 # incrementem el comte d'aparicions per aquesta vocal
    
    return dict(zip(vocals, aparicions)) # retornem un diccionari que associa cada vocal amb el seu nombre d'aparicions


#Programa principal:

paraula = input("Introdueix la paraula: ")
contadors = comptar_vocals(paraula)

for vocal, n in contadors.items():
    print(f"Hi ha {n} {vocal}'s")