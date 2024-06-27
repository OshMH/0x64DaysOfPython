import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
ORANGE = "#DC5F00"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.3
reps = 0
TICK = "✔"
ticks = ""
timer = None



# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global ticks
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(time_text,text="00:00")
    ticks = ""
    reps = 0
    tick_label.config(text=ticks)
    heading_label.config(text="Timer", fg=GREEN)
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    if reps == 7:
        heading_label.config(text="Long\nBreak", fg =RED)
        count_down(LONG_BREAK_MIN * 60)
        reps = 0
    elif reps % 2 == 0:
        heading_label.config(text="Work", fg =ORANGE)
        count_down(WORK_MIN * 60)
        reps += 1
    elif reps % 2 == 1:
        heading_label.config(text="Short\nBreak", fg =GREEN)
        count_down(SHORT_BREAK_MIN * 60)
        reps += 1
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# Using time is not good here.. Because we are using GUI the thread will get stuck in a while loop that is incrementing using time.sleep()
# We can using tkinter's after.

def count_down(count):
    global ticks
    # Zfill to pad with zeros
    count_min = str(math.floor(count / 60)).zfill(2)
    count_sec = str(count % 60).zfill(2)
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        if reps % 2 == 0:
            ticks += TICK
            
        tick_label.config(text=ticks)
        start_timer()


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
heading_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN)
heading_label
heading_label.grid(row=0, column=1)

# start button
start_button = tkinter.Button(text="Start", bg="white", highlightthickness=0, borderwidth=0, command=start_timer)
start_button.grid(row=2, column=0)
start_button.config(padx=1, pady=1)

# reset button
reset_button = tkinter.Button(text="Reset", bg="white", highlightthickness=0, borderwidth=0, command=reset_timer)
reset_button.config(padx=1, pady=1)
reset_button.grid(row=2, column=2)

# Tick
tick_label = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
tick_label.grid(row=3, column=1)


# left todo
# Handle multiple clicks of the start button
# Add functionality to reset.







window.mainloop()