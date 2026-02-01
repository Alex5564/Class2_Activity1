medical_cause=input("did you have a medical_cause: Y or N")
atten=int(input("Enter the attendance"))

if medical_cause=='Y':
 print("You are allowed")

else:
 if atten>=75:
  print("Allowed")
 else:
  print("Not allowed")