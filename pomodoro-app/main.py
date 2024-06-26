import tkinter


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# Using time is not good here.. Because we are using GUI the thread will get stuck in a while loop that is incrementing using time.sleep()
# We can using tkinter's after.

def start_timer(count):
    canvas.itemconfig(time_text, text=count)
    if count > 0:
        window.after(1000,start_timer, count-1)


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
window.minsize(width=300, height=324)
window.config(padx=50, pady=50, bg=YELLOW)

# Create the canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Timer label
timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN)
timer_label
timer_label.grid(row=0, column=1)

# start button
start_button = tkinter.Button(text="Start", bg="white", highlightthickness=0, borderwidth=0, command=lambda: start_timer(5))
start_button.grid(row=2, column=0)
start_button.config(padx=1, pady=1)

# reset button
reset_button = tkinter.Button(text="Reset", bg="white", highlightthickness=0, borderwidth=0)
reset_button.config(padx=1, pady=1)
reset_button.grid(row=2, column=2)

# Tick
tick_label = tkinter.Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
tick_label.grid(row=3, column=1)










window.mainloop()