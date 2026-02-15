String=input("Enter a character:")
Char=input("Enter your own character:")

i=0
count=0
while(i<len(String)):
    if(String[i]==Char):
      count=count+1
    i=i+1
print("The number of times", Char, "appears in the string is,:", count)