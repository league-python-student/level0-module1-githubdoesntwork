"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    val1=input("enter number\n")
    val2=input("enter another\n")
    val3=input("enter string\n")
    if(val3=="add"):
        print((int(val1)+int(val2)))
    elif(val3=="subtract"):
        print((int(val1)-int(val2)))
    elif (val3 == "multiply"):
        print((int(val1) * int(val2)))
    elif(val3=="divide"):
        print((float(val1)/float(val2)))