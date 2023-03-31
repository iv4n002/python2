longitud = int(input("Introduce la longitud del patrón: "))

for i in range(1, longitud+1):
    print("*" * i)
for i in range(longitud-1, 0, -1):
    print("*" * i)
