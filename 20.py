def binari_a_enter(binari):
    enter = 0
    for i in range(len(binari)):
        if binari[i] == '1':
            enter += 2 ** (len(binari) - 1 - i)
    return enter

if __name__ == '__main__':
    binari = input("Introdueix un número binari: ")
    enter = binari_a_enter(binari)
    print(f"El número binari {binari} en enter és {enter}.")
