def elements_parells(llista):
    for i in range(len(llista)):
        if i % 2 == 0:
            print(llista[i])

def main():
    paraules = input("Introdueix les paraules separades per espais: ").split()
    elements_parells(paraules)

if __name__ == '__main__':
    main()
