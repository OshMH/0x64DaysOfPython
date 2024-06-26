import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


#Label

def button_clicked():
    my_label["text"] = input.get()

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# This will place it on the screen. (pack())
my_label["text"] = "New text"
my_label.config(text="New text 2")
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)



button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

new_button = tkinter.Button(text="New button")
new_button.grid(row = 0, column=2)


#Entry
input = tkinter.Entry(width=10)
input.grid(row=3, column=3)


# .Place() will put things in a precise position.
# .Grid() thinks of the window as a grid of rows and columns. my_label.grid(column=0, row=5)
# We cant mix pack and grid in the same program.

window.mainloop()


def add(*args):
    total = 0
    for n in args:
        total += n
    
    return total


print(add(3,4,5,6,7,7))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
        # print(key)
        # print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
    
my_car = Car(make="Nissan")
print(my_car.model)