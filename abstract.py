class Vehicle:
    def start(self):
        print("Vehicle is starting...")

    def stop(self):
        print("Vehicle is stopping...")

class Car(Vehicle):
    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")

class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle is starting...")

    def stop(self):
        print("Motorcycle is stopping...")

car = Car()
car.start()
car.stop()

motorcycle = Motorcycle()
motorcycle.start()
motorcycle.stop()

vehicle = Vehicle()
vehicle.start()
vehicle.stop()



from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start_engine(self):
        pass

    def description(self):
        print(f"This is a vehicle of brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print(f"The {self.model} car from {self.brand} is starting its engine...")

    def description(self):
        super().description()
        print(f"Model: {self.model}")

# Test
try:
    vehicle = Vehicle("GenericBrand")  # This will raise an error since Vehicle is abstract
except TypeError as e:
    print(e)

car = Car("Toyota", "Corolla")
car.start_engine()
car.description()
