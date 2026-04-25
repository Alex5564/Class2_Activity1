class Dog:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
        
    def display_details(self):
        print(f"Dog Breed: {self.breed}, Color: {self.color}")

dog1 = Dog("Labrodor", "Yelloq")
dog2 = Dog("Pug", "Black")

dog1.display_details()
dog2.display_details()
