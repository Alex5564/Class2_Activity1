from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self, x):
        print(x)

    @abstractmethod
    def task(self):
        print("We are inside the abstract class")

class test_class(Absclass):
    def task(self):
        self.print("We are inside test_class task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)
