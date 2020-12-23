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
TICK = '✔'
reps = 0

count = 0
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global count
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = '00:00')
    tomato_label.config(text=' Timer ')
    tick_label.config(text='')
    count = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def pressed():
    global count
    count +=1
    if count == 1:start_timer()

def start_timer():
    global reps

    work_secs = WORK_MIN * 60
    short_rest_mins = SHORT_BREAK_MIN * 60
    long_rest_mins = LONG_BREAK_MIN * 60
    reps +=1

    if reps % 8 == 0:
        count_down(long_rest_mins)
        tomato_label.config(text='Rest 20', fg=RED)
            #reset_timer()
    elif reps % 2 == 0:
        count_down(short_rest_mins)
        tomato_label.config(text='Rest  5', fg=PINK)
    else:
        count_down(work_secs)
        tomato_label.config(text='Work 25', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def format_time_display(count):

    count_minute = math.floor(count // 60)
    count_seconds = count % 60
    if count_seconds < 10:
        return f'0:0{count_seconds}'
    else:
        return f'{count_minute}:{count_seconds}'

def count_down(count):

    time_display = format_time_display(count)
    canvas.itemconfig(timer_text, text = time_display )
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        if reps % 2 == 0:
            tick_label.config(text=TICK * (reps // 2))
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx = 100, pady=50, bg= YELLOW)


tomato_img = PhotoImage(file='tomato.png')

canvas = Canvas(width =320 , height =224, bg= YELLOW, highlightthickness=0)
canvas.create_image(160, 112, image= tomato_img)
timer_text = canvas.create_text(160,130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


tomato_label = Label(text='Timer',fg = GREEN, bg= YELLOW, font=(FONT_NAME, 72, 'bold'))
tomato_label.grid(column=1, row =0)

start_button = Button(text='Start', command=pressed)
start_button.grid(column=0,row=2)

stop_button = Button(text='Reset', command=reset_timer)
stop_button.grid(column=3, row=2)

tick_label = Label(fg= GREEN, bg= YELLOW, font=(FONT_NAME, 20, 'bold'))
tick_label.grid(column=1, row=3)


window.mainloop()

