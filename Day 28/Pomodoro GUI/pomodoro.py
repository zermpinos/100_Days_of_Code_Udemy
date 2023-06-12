# Heavily Modified Version 

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
remaining_time = 0
paused = False


def validate_timer_value(value, default_value):
    if not isinstance(value, int) or value <= 0:
        return default_value
    return value


WORK_MIN = validate_timer_value(WORK_MIN, 25)
SHORT_BREAK_MIN = validate_timer_value(SHORT_BREAK_MIN, 5)
LONG_BREAK_MIN = validate_timer_value(LONG_BREAK_MIN, 20)


def reset_timer():
    global reps, remaining_time, paused, timer
    reps = 0
    remaining_time = 0
    paused = False
    if timer is not None:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    start_button["state"] = NORMAL
    pause_button["state"] = DISABLED


def start_timer():
    global reps, paused, remaining_time
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    start_button["state"] = DISABLED
    pause_button["state"] = NORMAL

    if not paused:
        if reps % 8 == 0:
            remaining_time = long_break_sec
            title_label.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            remaining_time = short_break_sec
            title_label.config(text="Break", fg=PINK)
        else:
            remaining_time = work_sec
            title_label.config(text="Work", fg=GREEN)

    paused = False
    count_down(remaining_time)


def count_down(count):
    global remaining_time, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = "✔" * (reps // 2)
        check_marks.config(text=marks)

    remaining_time = count


def pause_timer():
    global timer, paused
    if timer is not None:
        window.after_cancel(timer)
    paused = True
    start_button["state"] = NORMAL


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer, state=NORMAL)
start_button.grid(column=0, row=2, pady=50)

pause_button = Button(text="Pause", highlightthickness=0, command=pause_timer, state=DISABLED)
pause_button.grid(column=1, row=2, pady=50)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2, pady=50)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
