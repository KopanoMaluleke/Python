import math

def draw_square(side_length):
    for i in range(side_length):
        print("*" * side_length)

print("Welcome to the Square !")

    # Menu options
print("Choose a shape to calculate its area and draw it:")


side_length = int(input("Enter the side length of the square: "))
print("This the square is:")
draw_square(side_length)

