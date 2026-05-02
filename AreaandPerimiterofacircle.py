class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159

    def area(self):
        return self.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * self.pi * self.radius

try:
    user_input = float(input("Enter the radius of circle: "))
    my_circle = Circle(user_input)
    
    print(f"Area: {my_circle.area():.2f}")
    print(f"Perimeter: {my_circle.perimeter():.2f}")
except ValueError:
    print("Please enter a valid number.")
