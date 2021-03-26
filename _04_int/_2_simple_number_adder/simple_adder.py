"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    val1=input("enter number\n")
    val2=input("enter another\n")
    print((int(val1)+int(val2)))