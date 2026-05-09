class A:
    
  def __init__(self, a):
   self.a=a
  
  def __it__(self, other):
   if self(self.a<other.a):
    return "obj1 is less than obj2"
    
   else:
    return "obj2 is less than obj1"

  def __eq__(self, other):
   if self(self.a==other.a):
    return "obj1 is equal to obj2"
   
   else:
    return "obj2 is equal to obj1"
    
    
ob1 = A(3)
ob2 = A(4)

print("Passed value:", ob1.a, ob2.a)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)

print("Passed value:", ob3.a, ob4.a)
print(ob3 == ob4)