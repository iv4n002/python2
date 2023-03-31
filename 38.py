numero = input("Introdueix un número:")
suma = 0

for digit in numero:
    suma += int(digit)
    
if suma % 2 == 0:
    print("La suma dels dígits és parella.")
else:
    print("La suma dels dígits és senar.")