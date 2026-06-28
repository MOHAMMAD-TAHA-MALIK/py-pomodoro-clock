from tkinter import *
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    s_break_sec = SHORT_BREAK_MIN * 60
    l_break_min = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        tim.config(text="BREAK", fg=PINK)
        count_down(l_break_min)

    elif reps % 2 == 0:
        tim.config(text="BREAK", fg=RED)
        count_down(s_break_sec)
    else:
        tim.config(text="WORK", fg=GREEN)
        count_down(work_sec)


def reset():
    global reps
    reps = 0
    tick.config(text="")
    window.after_cancel(timer)
    tim.config(text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")


def count_down(count):
    count_min = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"
    if count_second == 0:
        count_second = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(reps / 2)):
            mark += "✓"
        tick.config(text=mark)


window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)


tim = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
tim.grid(column=2, row=0)

canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="day-28/tomato.png")
canvas.create_image(100, 115, image=tomato)
timer_text = canvas.create_text(
    100, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=2, row=2)


start = Button(text="START", highlightthickness=0, command=start_timer)
start.grid(column=0, row=3)

tick = Label(bg=YELLOW, fg=GREEN)
tick.grid(column=2, row=3)

reset = Button(text="RESET", highlightthickness=0, command=reset)
reset.grid(column=4, row=3)

window.mainloop()