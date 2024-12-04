# Base Class: Vehicle
class Vehicle:
    def init(self, color):
        self.color = color  # Public attribute
    
    def vehicleInfo(self):
        return f"Vehicle Color: {self.color}"


# Derived Class: Taxi
class Taxi(Vehicle):
    def init(self, color, model, capacity):
        super().init(color)  # Initialize the base class
        self.__model = model  # Private attribute
        self.__capacity = capacity  # Private attribute
    
    # Getter for model
    def getModel(self):
        return self.__model
    
    # Setter for model
    def setModel(self, model):
        self.__model = model
    
    # Getter for capacity
    def getCapacity(self):
        return self.__capacity
    
    # Setter for capacity
    def setCapacity(self, capacity):
        self.__capacity = capacity
    
    # Overriding or extending vehicleInfo method
    def vehicleInfo(self):
        base_info = super().vehicleInfo()
        return f"{base_info}, Model: {self.model}, Capacity: {self.capacity}"


# Example usage:
if name == "main":
    # Create a Taxi object
    taxi1 = Taxi("Yellow", "Toyota Prius", 4)
    
    # Accessing and modifying attributes using getters and setters
    print(taxi1.vehicleInfo())
    taxi1.setModel("Honda Civic")
    taxi1.setCapacity(5)
    print(taxi1.vehicleInfo())