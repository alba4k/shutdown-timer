from tkinter import *

root = Tk()

choices = ['GB', 'MB', 'KB']
variable = StringVar(root)
variable.set('GB')

w = OptionMenu(root, variable, *choices)
w.pack()

root.mainloop()