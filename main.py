from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
tm = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer() -> None:
    global tm
    root.after_cancel(tm)
    
    global reps
    reps = 0
    
    checkmarks_label.config(text="")
    label.config(text="Timer", fg=GREEN)
    tomato.itemconfig(timer, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer() -> None:
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 2 != 0:
        countdown(10)
        label.config(text="Work", fg=GREEN)
    else:
        if reps == 8:
            countdown(10)
            label.config(text="Break", fg=RED)            
        else:
            countdown(10)
            label.config(text="Break", fg=PINK)
            
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count) -> None:
    global reps
    
    min = math.floor(count / 60)
    sec = count % 60
    
    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"
        
    tomato.itemconfig(timer, text=f"{min}:{sec}")
    if count > 0:
        global tm
        tm = root.after(1000, countdown, count - 1)
    else:
        start_timer()         
        checkmarks = "\u2713" * (int(reps / 2))
        checkmarks_label.config(text=checkmarks)
    
# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)

label = Label(root, text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

tomato = Canvas(root, width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
tomato.create_image(100, 112, image=img)
tomato.grid(row=1, column=1)

timer = tomato.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = Button(root, text="Start", font=(FONT_NAME, 8, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(root, text="Reset", font=(FONT_NAME, 8, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

checkmarks_label = Label(root, text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
checkmarks_label.grid(row=3, column=1)

root.mainloop()