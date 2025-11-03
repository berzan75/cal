from tkinter import *

t=Tk()
t.title("calculater")
t.geometry("400x400")

p= Label(t,
        text="calculator",font=("Times New Roman",15),bg="light blue")
p.place(x=130, y=20)

Time=Label(t,
        text="Enter In Time",font=("Times New Roman",9),bg="light blue")
Time.place(x=30, y=100)

speed=Label(t,
        text="Enter In Speed",font=("Times New Roman",9),bg="light blue")
speed.place(x=30, y=70)

entry_speed=Entry(t,
                  width=20,font=("Arial",10))
entry_speed.place(x=130, y=70)

a=Label(t,
        text="answer Is:",font=("Times New Roman",10),bg="light blue")
a.place(x=80, y=130)

entry_time=Entry(t,
            width=20,font=("Arial",10))
entry_time.place(x=130,y=100)

def cal():
    try:
        cal=float(entry_time.get())
        gal=float(entry_speed.get())
        distance=(cal*gal)
        a.config(text=f"distance:{distance:.1f}")
    except:
        a.config(text="please enter a valid number")

button=Button(t,
text="click me",command=cal)

button.place(x=180,y=150)

t.mainloop()