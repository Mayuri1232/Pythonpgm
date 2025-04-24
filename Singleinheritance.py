class Person:
    def get_details(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def get_student_info(self):
        self.roll_no = input("Enter roll number: ")
        self.course = input("Enter course: ")

    def display_student_info(self):
        self.display_details()
        print(f"Roll Number: {self.roll_no}")
        print(f"Course: {self.course}")

student = Student()
student.get_details()
student.get_student_info()
print("\n--- Student Information ---")
student.display_student_info()