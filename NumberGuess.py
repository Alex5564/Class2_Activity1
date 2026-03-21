import random 

number = random.randint (1,9)
while True:
  guess = int(input("guess a number between 1 and 9: "))
 
  if guess == number: 
    print("you guessed the number")
    break
    
  else:
    print("Try again")