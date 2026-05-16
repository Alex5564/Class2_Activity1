class RomanNumeralConverter:
    def int_to_roman(self, num: int) -> str:
        val_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        
        roman_num = ""
        for integer, roman in val_map:
            count = num // integer
            roman_num += roman * count
            num %= integer
            
        return roman_num


if __name__ == "__main__":
    converter = RomanNumeralConverter()
    
    try:
        user_input = int(input("Enter an integer to convert to Roman: "))
        if user_input > 0:
            result = converter.int_to_roman(user_input)
            print(f"The Roman numeral equivalent of {user_input} is: {result}")
        else:
            print("Please enter a positive integer greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
