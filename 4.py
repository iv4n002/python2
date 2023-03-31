def show_menu():
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicació")
    print("4. Divisió")
    print("5. Canvi de base")
    print("0. Sortir")

def get_input():
    while True:
        try:
            choice = int(input("Selecciona una opció: "))
            if choice < 0 or choice > 5:
                print("Opció no vàlida. Torna a intentar.")
                continue
            else:
                return choice
        except ValueError:
            print("Opció no vàlida. Torna a intentar.")

def get_number():
    while True:
        try:
            num = input("Introdueix un número: ")
            return int(num, 0)
        except ValueError:
            print("Entrada no vàlida. Torna a intentar.")

def convert_base():
    num = get_number()
    print("1. Binari")
    print("2. Octal")
    print("3. Decimal")
    print("4. Hexadecimal")
    choice = get_input()

    if choice == 1:
        print(f"{num} en binari és {bin(num)}")
    elif choice == 2:
        print(f"{num} en octal és {oct(num)}")
    elif choice == 3:
        print(f"{num} en decimal és {num}")
    elif choice == 4:
        print(f"{num} en hexadecimal és {hex(num)}")

def do_operation(operation):
    num1 = get_number()
    num2 = get_number()
    result = operation(num1, num2)
    print(f"El resultat és: {result}")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("No es pot dividir per zero.")
        return None
    else:
        return num1 / num2

while True:
    show_menu()
    choice = get_input()

    if choice == 0:
        print("Adéu!")
        break
    elif choice == 1:
        do_operation(add)
    elif choice == 2:
        do_operation(subtract)
    elif choice == 3:
        do_operation(multiply)
    elif choice == 4:
        do_operation(divide)
    elif choice == 5:
        convert_base()
