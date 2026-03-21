def validate_age():
    while True:
        try:
            age_input = int(input("Please enter your age: "))
            age = age_input
            if age < 1 or age > 120:
                raise ValueError("Age must be between 1 and 120.")
            break
        except ValueError as e:
            print(f"Invalid input: Please Try again {e}")
        except Exception as e:     
            print(f"An unexpected error occurred: Please Try again {e}")
    
    return age

def check_even_odd(age):
    if age % 2 == 0:
        print(f"{age} is an even number.")
    else:
        print(f"{age} is an odd number.")

if __name__ == "__main__":    
    valid_age = validate_age()
    print(f"Age Entered Successfully: {valid_age}")
    check_even_odd(valid_age)   