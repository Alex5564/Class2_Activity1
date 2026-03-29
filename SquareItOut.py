start = int(input("Enter start: "))
end = int(input("Enter end:" ))

squares = [i ** 2 for i in range(start, end + 1)]

evens = [n for n in squares if n % 2 == 0]
odds = [n for n in squares if n % 2 != 0]

print(f"Squares: {squares}")
print(f"Even Squares: {evens}")
print(f"Odds: {odds}")