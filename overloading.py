class Student:
    def __init__(self, *args):
        if len(args) == 0:
            self.name = "Unknown"
            self.age = 0
        elif len(args) == 1:
            self.name = args[0]
            self.age = 0
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        else:
            raise ValueError("Too many arguments")

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Example usage
s1 = Student()
s2 = Student("Alice")
s3 = Student("Bob", 22)

s1.display()  # Name: Unknown, Age: 0
s2.display()  # Name: Alice, Age: 0
s3.display()  # Name: Bob, Age: 22