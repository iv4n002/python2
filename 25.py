def es_de_traspas(anio):
    """Determina si el año dado es de traspaso o no"""
    
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    else:
        return False


# Programa principal

anio = int(input("Escribe un año: "))

if es_de_traspas(anio):
    print(f"{anio} es un año de traspaso")
else:
    print(f"{anio} no es un año de traspaso")