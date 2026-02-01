def is_alphabet(char):
    """
    Checks if the given character is an alphabet (a-z, A-Z).
    """
    if len(char) == 1 and char.isalpha():
        return True
    else:
        return False

user_input = input("Enter a single character: ")

if len(user_input) == 1:
    if is_alphabet(user_input):
        print(f"'{user_input}' is an alphabet.")
    else:
        print(f"'{user_input}' is not an alphabet (it's a number, symbol, or space).")
else:
    print("Invalid input. Please enter only a single character.")

