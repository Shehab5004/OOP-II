# Department Class
class Department:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Department Name: {self.name}")


# Teacher Class (inherits from Department)
class Teacher(Department):
    def schedule(self):
        print("Scheduling classes...")

    def grade_students(self):
        print("Grading students...")

    def display_name(self):
        print(f"Teacher belongs to Department: {self.name}")


# Author Class
class Author:
    def write_article(self):
        print("Writing an article...")

    def publish_blog(self):
        print("Publishing a blog...")


# TeacherAuthor Class (inherits from Teacher and includes Author functionality)
class TeacherAuthor(Teacher):
    def __init__(self, name):
        super().__init__(name)
        self.author = Author()  # Composition with Author

    def write_article(self):
        self.author.write_article()

    def publish_blog(self):
        self.author.publish_blog()


# Main Program
if name == "__main__":
    # Create a TeacherAuthor object
    teacher_author = TeacherAuthor("Computer Science")

    # Using methods from different classes
    teacher_author.display_name()
    teacher_author.schedule()
    teacher_author.grade_students()
    teacher_author.write_article()
    teacher_author.publish_blog()