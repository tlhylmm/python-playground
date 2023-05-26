from tkinter import *

# The code below used for including the image files into one executable with pyinstaller
# if used and when compiling to exe with pyinstaller, command down below needs to be used:
# pyinstaller --onefile --icon=icon.ico --windowed --add-data "icon.png;." --add-data "pomodoro.png;." main.py

# You can remove the part below but you also have to modify line 69 and 74
# and replace the resourcepath("filename.jpg") as "filename.jpg"
# but note that if you remove it, the exe won't work if the image files are not
# in the same folder with the executable file.
# Start of Code:
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#End of code

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
#time configuration (in minutes)
WORK = 25
SHORTBREAK = 5
LONGBREAK = 20

timer = None
reps = 0
def startTimer():
    global reps
    if (reps % 7 == 0) and (reps != 0):
        tickLabel["text"] += "✔|"
        topText.config(text="BREAK", fg=PINK)
        countdown(LONGBREAK*60)
    elif (reps % 2 == 1):
        tickLabel["text"] += "✔"
        topText.config(text="Break", fg=RED)
        countdown(SHORTBREAK*60)
    elif (reps % 2 == 0):
        topText.config(text="Work", fg=GREEN)
        countdown(WORK*60)
    reps += 1   

def countdown(seconds):
    canvas.itemconfig(timerText, text=f"{seconds//60:02d}:{seconds%60:02d}")
    if(seconds > 0):
        global timer
        timer = window.after(1000, countdown, seconds - 1)
    else:
        startTimer()

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00", fill="white")
    topText.config(text="Welcome",fg=GREEN)
    tickLabel["text"] = ""
    global reps
    reps = 0

# UI setup:
window = Tk()
window.title("tlhylmm's Pomodoro Clock")
icon = PhotoImage(file=resource_path("icon.png"))
window.iconphoto(False, icon)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file=resource_path("pomodoro.png"))
canvas.create_image(100, 112, image=img)

timerText = canvas.create_text(110, 130, text="00:00", fill="white", font=("Courier", 30, "bold"))
canvas.grid(column=1, row= 1)

topText = Label(text="Welcome", fg=GREEN, bg=YELLOW, font=("Courier", 50))
topText.grid(column=1, row=0)

authorLabel = Label(text="Made by Talha Yılmam in 2022",
                    font = ("Courier", 8), bg=YELLOW)
authorLabel.grid(column=1,row=4)

#Label for adding "✔" symbol at the end of each completed work (start as empty) 
tickLabel = Label(text="", fg = "#379B46", bg=YELLOW, font=("Arial", 18))
tickLabel.grid(column=1, row=3)

startButton = Button(text="START", fg="#379B46",bg="#F7F0A5", font=("Arial",16,"bold"),
                    width=7, height=1, command=startTimer)
startButton.grid(column=0, row=2)

resetButton = Button(text="RESET", fg=RED,bg="#F7F0A5", font=("Arial",16,"bold"),
                    width=7, height=1, command= reset)
resetButton.grid(column=2, row=2)

window.mainloop()