data= [(1, '10A', 'Math'), (2, '10B', 'Science'), (1, '10A', 'Math'), (3, '10B', 'English'), (2, '10B', 'Science')]

unique_data = list(set(data))

for item in unique_data:
 print(item)