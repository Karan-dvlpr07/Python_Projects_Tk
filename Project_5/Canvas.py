
from tkinter import *

root = Tk()
root.geometry('400x400')

# Canvas

C = Canvas(root, width=600, height=600)
C.pack()

C.create_rectangle(150,125,450,375,fill="yellow")

root.mainloop()