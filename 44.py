def elimina_duplicats(llista):
    return list(set(llista))

# Ejemplo de uso
llista = input("Introduce una lista de números separados por comas: ").split(",")
llista = [int(num) for num in llista] # Convertir elementos de la lista a números enteros
llista_sense_duplicats = elimina_duplicats(llista)
print("Llista original:", llista)
print("Llista sense duplicats:", llista_sense_duplicats)
