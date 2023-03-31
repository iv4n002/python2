def main():
    paraula1 = input("Introdueix la primera paraula: ")
    paraula2 = input("Introdueix la segona paraula: ")

    if rimen(paraula1, paraula2, 3):
        print("Les paraules rimen.")
    elif rimen(paraula1, paraula2, 2):
        print("Les paraules rimen un poc.")
    else:
        print("Les paraules no rimen.")

def rimen(paraula1, paraula2, num_lletres):
    return paraula1[-num_lletres:] == paraula2[-num_lletres:]

if __name__ == "__main__":
    main()