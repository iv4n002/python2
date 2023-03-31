num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

suma = 0
for i in range(num1, num2+1):
    suma += i

print("La suma de todos los números entre", num1, "y", num2, "es:", suma)
