# Obtenim l'entrada de l'usuari per al número de la taula de multiplicar
num = int(input("Introdueix un número per a obtenir-ne la taula de multiplicar: "))

# Imprimim les 20 primeres files (de 1 a 20) amb el valor del número entrat i el seu producte  
for i in range(1,21):
   print(num," x ",i," = ",num*i)