from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("i can walk and run")

class Snake(Animal):

    def move(self):
        print("i can crawl")

class Dog(Animal):

    def move(self):
        print("i can bark")

class Lion(Animal):

    def move(self):
        print("i can roar")

h = Human()
h.move

s = Snake()
s.move()

d = Dog()
d.move()

l = Lion()
l.move()