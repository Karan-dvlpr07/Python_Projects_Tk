
from tkinter import *

root = Tk()
root.geometry('400x400')

# Canvas

C = Canvas(root, width=600, height=600)
C.pack()

C.create_oval(100,100,200,200, width=2, fill="orange")

root.mainloop()