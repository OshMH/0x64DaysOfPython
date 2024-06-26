import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


miles_input = tkinter.Entry(width=7)
miles_input.grid(row=0, column=1)
miles_label = tkinter.Label()
miles_label["text"] = "Miles"
miles_label.grid(row=0, column=2)


is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(row=1, column=0)


km_result = tkinter.Label(text="0")
km_result.grid(row=1, column=1)
km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

def convert_values():
    miles = miles_input.get()
    if not miles.isalnum():
        print("not a number")
    else:
        km_result["text"] = str(float(miles) * 1.60934)

calculate_button = tkinter.Button(text="Calculate", command=convert_values)
calculate_button.grid(row=2, column=1)













window.mainloop()