from tkinter import Tk, Text, INSERT, END

from tkinter import *

def onclick():
   pass

root = Tk()
text = Text(root)
text.configure(state='normal')
text.insert('end', 123)
text.configure(state='disabled')
text.pack()

root.mainloop()