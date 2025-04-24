class Shape:
    def area(self, *args):
        if len(args) == 1:
            side = args[0]
            print(f"Area of square: {side * side}")
        elif len(args) == 2:
            length, breadth = args
            print(f"Area of rectangle: {length * breadth}")
        else:
            print("Invalid number of arguments")

# Example usage:
shape = Shape()

# Area of square
shape.area(5)

# Area of rectangle
shape.area(4, 6)