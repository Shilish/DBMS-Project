from tkinter import *
from  tkinter import messagebox
import  cx_Oracle
from PIL import Image, ImageTk
root = Tk()

root.title("pack demo")
root.config(bg='#A3E4D7')
root.geometry("400x400")
f_name = Entry(root, width=30)
f_name.pack()

root.mainloop()