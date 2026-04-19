num_limit = int(input("Enter a Number: "))

odd_numbers = [x for x in range (num_limit) if x % 2 != 0]

print(f"Odd numbers under {num_limit}: {odd_numbers}")

fruit = ["apple", "banana", "cherry", "date", "elderberry"]
capitalized_fruits = [fruit.capitalize() for fruit in fruit]

print(f"Updated Fruit List: {capitalized_fruits}")