class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_details(self):
        print(f"Product Name: {self.name}, Price: {self.price}")

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display_details(self):
        super().display_details()
        print(f"Warranty: {self.warranty} years")

# Example
p = Product("Notebook", 20)
p.display_details()

e = ElectronicProduct("Laptop", 1500, 2)
e.display_details()


class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def display_info(self):
        print(f"Shape Name: {self.name}")

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def display_info(self):
        super().display_info()
        print(f"Length: {self.__length}, Width: {self.__width}")
        print(f"Area: {self.area()}, Perimeter: {self.perimeter()}")

# Example
r = Rectangle("Rectangle", 10, 5)
r.display_info()
