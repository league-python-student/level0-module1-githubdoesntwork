"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
import turtle
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    ans=input("type something\n")
    val=0
    if(ans=="something"):
        val=val+1
    ans = input("the answer to the last question was 'something'\n")
    if (ans == "how did you get this right"):
        val = val + 1
    ans = input("I forgot to ask a question in the last one\n")
    if (ans == "actually how"):
            val = val + 1

    ans = input("Oops, I did it again\n")
    if (ans == "bruh"):
        val = val + 1
    print("Wow, you only got "+str(val)+" questions right smh")