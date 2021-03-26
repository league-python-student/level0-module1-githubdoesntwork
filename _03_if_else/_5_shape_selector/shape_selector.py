import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    bruh = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    val = input("Enter your shape: ")
    # Draw the shape requested by the user using if-elif-else statements
    if(val=="insert obscure shape name for square"):
        bruh.pendown()
        bruh.forward(100)
        bruh.right(90)
        bruh.forward(100)
        bruh.right(90)
        bruh.forward(100)
        bruh.right(90)
        bruh.forward(100)
    # Call bruh turtle .done() method
    turtle.done
