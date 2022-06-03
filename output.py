from tkinter import *
from  tkinter import messagebox
import  cx_Oracle

window = Tk()

window.title("Train Ticket Booking System_A_Shilish, Rohan & Anantha")
window.config(bg='#5d6466')
window.geometry("1280x720")

### defining output button for the TRAIN_INFO table
def output_train_info():
    conn = cx_Oracle.connect('system/ayonya123@localhost')
    c = conn.cursor()
    c.execute("select * from train_info",{
              })
    out = c.fetchall()
    train_info.insert(END, out)
    #print(out)
    #messagebox.showinfo("Success","Data Displayed from TRAIN_INFO")


    conn.commit()
    conn.close()

def output_passenger():
    conn = cx_Oracle.connect('system/ayonya123@localhost')
    c = conn.cursor()
    c.execute("select * from passenger",{
              })
    out = c.fetchall()
    train_info.insert(END, out)
    #print(out)
    #messagebox.showinfo("Success","Data Displayed from PASSENGER")


    conn.commit()
    conn.close()

def output_ticket():
    conn = cx_Oracle.connect('system/ayonya123@localhost')
    c = conn.cursor()
    c.execute("select * from ticket",{
              })
    out = c.fetchall()
    train_info.insert(END, out)
    #print(out)
    #messagebox.showinfo("Success","Data Displayed from TICKET")


    conn.commit()
    conn.close()

### create text boxes for TRAIN_INFO OUTPUT
train_info = Entry(window, width=30)
train_info.place(x=200, y=300, width=800, height=400)

### creating output buttons
output_train_info_button = Button(window, text="Display  ->  'TRAIN_INFO'", command=output_train_info)
output_train_info_button.place(x=100, y=200, width=300, height=50)

output_passenger_button = Button(window, text="Display  ->  'PASSENGER'", command=output_passenger)
output_passenger_button.place(x=450, y=200, width=300, height=50)

output_ticket_button = Button(window, text="Display  ->  'TICKET'", command=output_ticket)
output_ticket_button.place(x=800, y=200, width=300, height=50)


window.mainloop()