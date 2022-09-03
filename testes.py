from tkinter import *
from tkcalendar import *
from datetime import date

root = Tk()
root.title('FF')
root.geometry("600x400")

cal = Calendar(root, selectmode="day", year=date.today().year, month=date.today().month, day=date.today().day)

cal.pack()

def grab_date():
    my_label.config(text="Date is " + cal.get_date())

my_button = Button(root, text="GEt Date", command=grab_date)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()
