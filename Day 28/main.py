from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#ebdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# Reset timer
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00 : 00")
    timer_label.config(text="TIMER")
    check_label.config(text="")
    global reps
    reps = 0


# Start Timer
def start_timer():
    global reps
    reps += 1
    seconds = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break)
    else:
        timer_label.config(text="WORK ", fg=GREEN)
        count_down(seconds)


# Countdown
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes} : {seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_mark = ""
        for i in range(0, math.floor(reps/2)):
            check_mark += "✔"
        check_label.config(text=check_mark)


# UI
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)

timer_text = canvas.create_text(100, 130, text="00 : 00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(fg=PINK, bg=YELLOW, font=(FONT_NAME, 25))
check_label.grid(row=3, column=1)

window.mainloop()
