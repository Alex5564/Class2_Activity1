num_str=input("Enter a number: ")

num=int(num_str)
reverse_str=""

while num>0:    
    digit=num%10
    reverse_str=reverse_str+str(digit)
    num=num//10 

print("Reversed number:", reverse_str)