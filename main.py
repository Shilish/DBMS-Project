from tkinter import *
from  tkinter import messagebox
import  cx_Oracle

window = Tk()

window.title("Train Ticket Booking System_A_Shilish, Rohan & Anantha")
window.config(bg='#16703a')
window.geometry("1280x720")


### defining submit button for the TRAIN_INFO table
def submit_train_info():
    conn = cx_Oracle.connect('system/ayonya123@localhost')
    c = conn.cursor()
    c.execute("Insert into train_info (train_number,train_name,distance,class,available_seats,source,departure_time,arrival_time,travel_time,journey_date) values (&train_number, &train_name, &distance, &class, &available_seats, &source, &departure_time, &arrival_time, &travel_time, &journey_date)",{
                  'train_number': train_number1.get(),
                  'train_name': train_name.get(),
                  'distance': distance.get(),
                  'class': class_train.get(),
                  'available_seats': available_seats.get(),
                  'source': source.get(),
                  'departure_time': departure_time.get(),
                  'arrival_time': arrival_time.get(),
                  'travel_time': travel_time.get(),
                  'journey_date': journey_date1.get(),
              })
    messagebox.showinfo("Success", "Data Added to the 'train_info' table")


    conn.commit()
    conn.close()


    train_number1.delete(0, END)
    train_name.delete(0, END)
    distance.delete(0, END)
    class_train.delete(0, END)
    available_seats.delete(0, END)
    source.delete(0, END)
    departure_time.delete(0, END)
    arrival_time.delete(0, END)
    travel_time.delete(0, END)
    journey_date1.delete(0, END)



### defining submit button for the PASSENGER table
def submit_passenger():
    conn = cx_Oracle.connect('system/ayonya123@localhost')
    c = conn.cursor()
    c.execute("Insert into passenger (passenger_id,name,age,contact_number,train_number,fare,berth,journey_date) values (&passenger_id, &name, &age, &contact_number, &train_number, &fare, &berth, &journey_date)",{
                  'passenger_id': passenger_id.get(),
                  'name': name.get(),
                  'age': age.get(),
                  'contact_number': contact_number.get(),
                  'train_number': train_number2.get(),
                  'fare': fare.get(),
                  'berth': berth.get(),
                  'journey_date': journey_date2.get(),
              })
    messagebox.showinfo("Success","Data Added to the 'passenger' table")


    conn.commit()
    conn.close()


    passenger_id.delete(0, END)
    name.delete(0, END)
    age.delete(0, END)
    contact_number.delete(0, END)
    train_number2.delete(0, END)
    fare.delete(0, END)
    berth.delete(0, END)
    journey_date2.delete(0, END)


### defining submit button for the TICKET table
def submit_ticket():
    conn = cx_Oracle.connect('system/ayonya123@localhost')
    c = conn.cursor()
    c.execute("Insert into ticket (transaction_id,pnr_number,train_number,passenger_name,journey_date) values (&transaction_id, &pnr_number, &train_number, &passenger_name, &journey_date)",{
                  'transaction_id' : transaction_id.get(),
                  'pnr_number' : pnr_number.get(),
                  'train_number' : train_number3.get(),
                  'passenger_name' : passenger_name.get(),
                  'journey_date' : journey_date3.get(),
              })
    messagebox.showinfo("Success","Data Added to the 'ticket' table")


    conn.commit()
    conn.close()


    transaction_id.delete(0, END)
    passenger_name.delete(0, END)
    pnr_number.delete(0, END)
    train_number3.delete(0, END)
    journey_date3.delete(0, END)


### create text boxes for TRAIN_INFO table
train_number1 = Entry(window, width=30)
train_number1.place(x=210, y=100)

train_name = Entry(window, width=30)
train_name.place(x=210, y=125)

distance = Entry(window, width=30)
distance.place(x=210, y=150)

class_train = Entry(window, width=30)
class_train.place(x=210, y=175)

available_seats = Entry(window, width=30)
available_seats.place(x=210, y=200)

source = Entry(window, width=30)
source.place(x=210, y=225)

departure_time = Entry(window, width=30)
departure_time.place(x=210, y=250)

arrival_time = Entry(window, width=30)
arrival_time.place(x=210, y=275)

travel_time = Entry(window, width=30)
travel_time.place(x=210, y=300)

journey_date1 = Entry(window, width=30)
journey_date1.place(x=210, y=325)


### create text box labels for TRAIN_INFO table
train_number1_label = Label(window, text="Train Number (PK)") 
train_number1_label.place(x=100, y=100, width=105)

train_name_label = Label(window, text="Train Name")
train_name_label.place(x=100, y=125, width=105)

distance_label = Label(window, text="Distance")
distance_label.place(x=100, y=150, width=105)

class_train_label = Label(window, text="Class")
class_train_label.place(x=100, y=175, width=105)

available_seats_label = Label(window, text="Available Seats")
available_seats_label.place(x=100, y=200, width=105)

source_label = Label(window, text="Source")
source_label.place(x=100, y=225, width=105)

departure_time_label = Label(window, text="Departure Time")
departure_time_label.place(x=100, y=250, width=105)

arrival_time_label = Label(window, text="Arrival Time")
arrival_time_label.place(x=100, y=275, width=105)

travel_time_label = Label(window, text="Travel Time")
travel_time_label.place(x=100, y=300, width=105)

journey_date1_label = Label(window, text="Journey Date")
journey_date1_label.place(x=100, y=325, width=105)



### create text boxes for PASSENGER table
passenger_id = Entry(window, width=30)
passenger_id.place(x=610, y=100)

name = Entry(window, width=30)
name.place(x=610, y=125)

age = Entry(window, width=30)
age.place(x=610, y=150)

contact_number = Entry(window, width=30)
contact_number.place(x=610, y=175)

train_number2 = Entry(window, width=30)
train_number2.place(x=610, y=200)

fare = Entry(window, width=30)
fare.place(x=610, y=225)

berth = Entry(window, width=30)
berth.place(x=610, y=250)

journey_date2 = Entry(window, width=30)
journey_date2.place(x=610, y=275)


### create text box labels for PASSENGER table
passenger_id_label = Label(window, text="Passenger ID (PK)") 
passenger_id_label.place(x=500, y=100, width=105)

name_label = Label(window, text="Name")
name_label.place(x=500, y=125, width=105)

age_label = Label(window, text="Age")
age_label.place(x=500, y=150, width=105)

contact_number_label = Label(window, text="Contact Number")
contact_number_label.place(x=500, y=175, width=105)

train_number2_label = Label(window, text="Train Number (FK)")
train_number2_label.place(x=500, y=200, width=105)

fare_label = Label(window, text="Fare")
fare_label.place(x=500, y=225, width=105)

berth_label = Label(window, text="Berth")
berth_label.place(x=500, y=250, width=105)

journey_date2_label = Label(window, text="Journey Date")
journey_date2_label.place(x=500, y=275, width=105)



### create text boxes for TICKET table
transaction_id = Entry(window, width=30)
transaction_id.place(x=1010, y=100)

pnr_number = Entry(window, width=30)
pnr_number.place(x=1010, y=125)

train_number3 = Entry(window, width=30)
train_number3.place(x=1010, y=150)

passenger_name = Entry(window, width=30)
passenger_name.place(x=1010, y=175)

journey_date3 = Entry(window, width=30)
journey_date3.place(x=1010, y=200)


### create text box labels for TICKET table
transaction_id_label = Label(window, text="Transaction ID (PK)") 
transaction_id_label.place(x=900, y=100, width=105)

pnr_number_label = Label(window, text="PNR Number")
pnr_number_label.place(x=900, y=125, width=105)

train_number3_label = Label(window, text="Train Number (FK)")
train_number3_label.place(x=900, y=150, width=105)

passenger_name_label = Label(window, text="Passenger Name")
passenger_name_label.place(x=900, y=175, width=105)

journey_date3_label = Label(window, text="Journey Date")
journey_date3_label.place(x=900, y=200, width=105)


### creating insertion buttons
submit_train_info_button = Button(window, text="Insert into  ->  'TRAIN_INFO'", command=submit_train_info)
submit_train_info_button.place(x=100, y=375, width=300, height=50)

submit_passenger_button = Button(window, text="Insert into  ->  'PASSENGER'", command=submit_passenger)
submit_passenger_button.place(x=500, y=375, width=300, height=50)

submit_ticket_button = Button(window, text="Insert into  ->  'TICKET'", command=submit_ticket)
submit_ticket_button.place(x=900, y=375, width=300, height=50)

window.mainloop()