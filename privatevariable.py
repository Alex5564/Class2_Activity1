class myclass:

 __privateVar = 27

 def __privMeth(self):
  print("I am inside my class")

 def hello(self):
  print("Private variable value: ", myclass.__privateVar)
  self.__privMeth()

son = myclass()
son.hello()