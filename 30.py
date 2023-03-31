num = int(input("Introduïu un número menor que 100: "))
total = 0
for n in range(num, 0, -4):
    if (n - 4) > 0:
        total += (n-4)**2
        
print(f"La suma dels quadrats és {total}")