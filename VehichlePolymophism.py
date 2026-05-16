class BMW:

    def fuel_type(self):
        print("BMW uses deisel")

    def max_speed(self):
        print("BMW has a max speed of 250 km/h")

class Ferrari:

    def fuel_type(self):
        print("Ferrari uses petrol")

    def max_speed(self):
        print("Ferrari has a max speed of 340 km/h")


bmw_car = BMW() 
ferrari_car = Ferrari()

bmw_car.fuel_type()
bmw_car.max_speed()
ferrari_car.fuel_type()
ferrari_car.max_speed()
