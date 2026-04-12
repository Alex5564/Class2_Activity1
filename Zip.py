list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

result = zip(list1, list2)
print(list(result))

name = [ "Alice", "Bob", "Charlie", "David", "Eve" ]
age = [ 25, 30, 35, 40, 45 ]

dict = {name: age for name, age in zip(name, age)}
print(dict)

