class Father:
    def show_father(self):
        print("This is the Father class.")

class Mother:
    def show_mother(self):
        print("This is the Mother class.")

class Child(Father, Mother):
    def show_child(self):
        print("This is the Child class.")

# Create object of Child class
child = Child()

child.show_father()
child.show_mother()
child.show_child()