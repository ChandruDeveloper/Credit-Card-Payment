from ctypes import alignment
from lib2to3.pgen2.token import NUMBER
from tarfile import SOLARIS_XHDTYPE
from this import d
from tkinter import *
from tkinter import colorchooser


ws = Tk()
ws.title('Credit Card Payment')
ws.geometry("700x800")
ws.config(bg='#0B5A81')

f = ('Times', 14)
var = StringVar()
var.set('male')




right_frame = Frame(
    ws, 
    bd=2, 
    bg='grey',
    relief=SOLID, 
    padx=20, 
    pady=20,
    cursor=NONE
    )


Label (
    right_frame, 
    text="Credit Card", 
  
    bg='green',
    font=d
    ).grid(row=0, column=0, sticky=W, pady=10)


Label(
    right_frame, 
    text="CARD NUMBER", 
    bg='white',
    font=d
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="EXPIRY MONTH", 
    bg='white',

    font=d
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="YEAR", 
    bg='white',
    font=d
    ).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="CVV", 
    bg='white',
    font=d
    ).grid(row=3, column=0, sticky=W, pady=10,columnspan=20)


   

label= Label(ws, text= "PAYMENT DETAILS", font= ("D", 10))
label.pack(pady=30)





register_num = Entry(
    right_frame, 
    font=f
    )

register_mon= Entry(
   

    right_frame, 
    font=f
    )

register_yr = Entry(
    right_frame, 
    font=f
    )
register_cvv = Entry(
    right_frame, 
    font=f
    )
register_btn = Button(
    right_frame, 
    width=15, 
    text='Submit', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=None
)


register_num.grid(row=0, column=1, pady=10, padx=20)
register_mon.grid(row=1, column=1, pady=10, padx=20) 
register_yr.grid(row=2, column=1, pady=10, padx=20)
register_cvv.grid(row=3, column=1, pady=10, padx=20)
register_btn.grid(row=4, column=1, pady=10, padx=20)
right_frame.pack()




ws.mainloop()