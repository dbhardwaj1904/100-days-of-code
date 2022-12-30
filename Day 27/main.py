from tkinter import *


def convert_miles_to_km():
    miles = float(input_miles.get())
    km = round(miles * 1.689)
    km_calculated.config(text=f"{km}")


window = Tk()
window.title("Mile/s to Km Converter")
window.config(padx=70, pady=10)

input_miles = Entry(width=10)
input_miles.grid(row=0, column=1)

label_miles = Label(text="\n\nMiles")
label_miles.grid(row=0, column=2)

label_equal_to = Label(text="is equal to")
label_equal_to.grid(row=1, column=0)

km_calculated = Label(text="0")
km_calculated.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
