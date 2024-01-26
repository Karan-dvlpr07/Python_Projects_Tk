from tkinter import *

root = Tk()
root.geometry('400x400')

# Canvas

C = Canvas(root, width=600, height=600)
C.pack()
C.create_line(0,0,600,600, width=5, fill="orange" , dash=(3,3))


root.mainloop()