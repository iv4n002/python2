import random

def generate_code():
    code = []
    for _ in range(4):
        code.append(random.randint(0, 9))
    return code

def evaluate_guess(code, guess):
    num_correct_pos = sum([code[i] == guess[i] for i in range(4)])
    num_correct_num = len(set(code) & set(guess)) - num_correct_pos
    print(f"Posiciones correctas: {num_correct_pos}")
    print(f"Numeros correctos pero posiciones incorrectas: {num_correct_num}")

if __name__ == "__main__":
    print("Bienvenido a MasterMind de ivan!")
    
    # Generate secret code
    secret_code = generate_code()
    
    while True:
        # Prompt user for guess and validate input
        try:
            user_input_str = input("Pon tu codigo (4 digits): ")
            if len(user_input_str) != 4:
                raise ValueError()
            user_guess = [int(digit) for digit in user_input_str]
        except ValueError:
            print("Invalida. Pon echactamente los numeros.")
            continue
        
        # Evaluate guess and check for win condition
        evaluate_guess(secret_code, user_guess)
        if secret_code == user_guess:
            break
    
    print("Felicidades, Has acertado el codigo.")

