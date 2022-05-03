from tkinter import *
from tkinter import messagebox



window = Tk() 
window.title("Welcome!")
window.geometry("300x200")



en1 = Entry(window)
en1_label = Label(window,text='Enter price:')
en1_label.grid(row=0, column=0)
en1.grid(row=0, column=1)

en2 = Entry(window)
en2_label = Label(window,text='Enter shipping:')
en2_label.grid(row=1, column=0)
en2.grid(row=1, column=1)

en3 = Entry(window)
en3_label = Label(window,text='Enter profit in % :')
en3_label.grid(row=2, column=0)
en3.grid(row=2, column=1)

def calcWithTax():
    output.delete(0, END)
    profit = float(float(en3.get())/100)
    price = float(en1.get())
    shipping = float(en2.get())
    answer = ((price + (price * profit)) *1.25) + shipping
    output.insert(0,answer)


def calcWithoutTax():
    output.delete(0, END)
    profit = float(float(en3.get())/100)
    price = float(en1.get())
    shipping = float(en2.get())
    answer = (price + (price * profit)) + shipping 
    output.insert(0,answer)


btnWithTax = Button(window,text="with tax",bg='black', fg='white',command=calcWithTax)
btnWithTax.grid(row=4,column=1)


btnWithoutTax = Button(window,text="without tax",bg='black', fg='white',command=calcWithoutTax)
btnWithoutTax.grid(row=5,column=1)


output_label = Label(window,text='Price:')
output_label .grid(row=6, column=0)
output = Entry(window)
output.grid(row=6,column=1)

window.mainloop()