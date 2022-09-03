from tkinter import *
from tkcalendar import  *
from datetime import date

root = Tk()
root.title('FF')
root.geometry("600x400")

cal = Calendar(root, selectmode="day", year=date.today().year, month=date.today().month, day=date.today().day)

cal.pack()

def grab_date():