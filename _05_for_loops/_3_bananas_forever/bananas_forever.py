"""
 * Write a python program that prints the word 'banana' one thousand (1,000) times
"""

from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    for i in range(1000):
        print("banana")