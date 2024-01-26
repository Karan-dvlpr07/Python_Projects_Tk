from tkinter import *
import tkinter as tk

root = Tk()
root.geometry('400x400')

b = Button(root, text="click here", activebackground= "orange", activeforeground= "white" )
b.pack()

root.mainloop()