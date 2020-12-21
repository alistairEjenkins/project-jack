import tkinter

window = tkinter.Tk()
window.title("My Miles to KM converter")
window.minsize(width=250, height=80)

def convert_miles_to_km():

    km = str(round(int(input_miles.get()) * 2.2,0))
    display_km['text'] = km

is_equal_to = tkinter.Label(text='is equal to', font=('Arial'), anchor='e')
is_equal_to.grid(column=0,row=1)

input_miles = tkinter.Entry(width = 10)
input_miles.grid(column=1,row=0)

display_km = tkinter.Label(text='0', font=('Arial'))
display_km.grid(column=1,row=1)

calculate = tkinter.Button(text='Calculate', command=convert_miles_to_km)
calculate.grid(column=1,row=2)


miles = tkinter.Label(text='Miles', padx=-50, font=('Arial'))
miles.grid(column=2,row=0)

km = tkinter.Label(text='Km', padx=-50, font=('Arial'))
km.grid(column=2,row=1)




window.mainloop()