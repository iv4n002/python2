num = int(input("Introdueix el teu número: "))

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        print(digit)
    num //= 10