def avaluar_majuscules(cadena):
    count = 0
    for car in cadena:
        if car.isupper():
            count += 1
    return count

if __name__ == '__main__':
    cadena = input("Introduce una cadena de texto: ")
    num_majusculas = avaluar_majuscules(cadena)
    print(f"La cadena '{cadena}' contiene {num_majusculas} letras mayúsculas.")
