class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        print("Student Constructor")
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


class Alumni(Student):
    def __init__(self, fname, lname, year):
        print("Alumni Constructor")
        super().__init__(fname, lname, year)
        self.passing_year = 2018

    def display(self):
        print(self.passing_year)


class Current(Student):
    def __init__(self, fname, lname, year):
        print("Current Constructor")
        super().__init__(fname, lname, year)
        self.current_semester = 6

    def display(self):
        print(self.current_semester)


class CSE_student(Alumni, Current):
    def __init__(self, fname, lname, year):
        print("CSE_student Constructor")
        super().__init__(fname, lname, year)


# Creating instances and calling methods
x = CSE_student("Mike", "Olsen", 2024)
y = Student("Hero", "Alam", 2024)
z = Current("Alu", "Alu", 2024)

x.welcome()  # Welcome message from CSE_student
y.welcome()  # Welcome message from Student
z.display()  # Display current semester


class Teacher(Person):
    def __init__(self, fname, lname, year):
        print("Teacher Constructor")
        super().__init__(fname, lname)
        self.joiningyear = year

    def welcome(self):
        print("welcome", self.firstname, self.lastname, "to take the class of", self.joiningyear)


a = Teacher("Mikel", "Jackson", 2022)
b = Teacher("Jayed", "Khan", 2022)
a.welcome()
b.welcome()


class Admin(Person):
    def __init__(self, fname, lname, year):
        print("Admin Constructor")
        super().__init__(fname, lname)
        self.joiningyear = year

    def welcome(self):
        print("welcome", self.firstname, self.lastname, "to the admin panel", self.joiningyear)


m = Admin("Bruce", "Lee", 2022)
n = Admin("Mahfujur", "Rahman", 2022)
m.welcome()
n.welcome()
