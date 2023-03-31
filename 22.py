def mostrar_majors_que(tupla, num):
    for elem in tupla:
        if elem > num:
            print(elem)


tupla = tuple(map(int, input("Introduce los valores enteros de la tupla separados por comas: ").split(",")))
num = 18
print("Los valores de la tupla mayores que", num, "son:")
mostrar_majors_que(tupla, num)
