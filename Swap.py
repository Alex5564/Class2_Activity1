
def swap_three_numbers(a, b, c):
    print(f"Original values: a = {a}, b = {b}, c = {c}")
    
    a, b, c = c, a, b
    
    print(f"Swapped values:  a = {a}, b = {b}, c = {c}")
    print("-"* 20)

num1, num2, num3 = 10, 20, 30
swap_three_numbers(num1, num2, num3)

x, y, z = "Apple", 42, 9.9
swap_three_numbers(x, y, z)
