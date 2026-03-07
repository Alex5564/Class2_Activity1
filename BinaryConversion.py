def decimal_to_binary_nested(n):
    if n == 0: 
     return "0"      
    binary_str = ""
    while n > 0:
        remainder = n % 2
        for _ in range(1):
         binary_str = str(remainder) + binary_str
        n = n // 2
    
    return binary_str

num = 25
print(f"Decimal: {num} -> Binary: {decimal_to_binary_nested(num)}")