import tkinter as tk
import os

display=tk.Tk(className="\nShutdown")
display.geometry("315x330")
#display.iconbitmap("shutdown/icon.ico")
command,hours,minutes,seconds=tk.StringVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()

def _confirm():
    time=str(seconds.get()+minutes.get()*60+hours.get()*3600)
    if command.get() == "shutdown":
        os.system("shutdown /s /t "+time)
    elif command.get() == "restart":
        os.system("shutdown /r /t "+time)
    elif command.get() == "disconnect":
        os.system("shutdown /l")

def theme_check():
    global current_theme
    file = open(r"shutdown/.settings", "w")
    if(not current_theme):    # dark
        file.write("1")
        current_theme = 1
        display.config(bg = "#1C1C1C")
        version.config(bg="#1C1C1C", fg="#F0F0F0")
        confirm.config(bg="#116611", fg="#F0F0F0", activebackground = "#116611", activeforeground="#F0F0F0")
        cancel.config(bg="#661111", fg="#F0F0F0", activebackground = "#661111", activeforeground="#F0F0F0")
        theme.config(bg="#252525", fg = "#F0F0F0", activebackground = "#252525", activeforeground="#F0F0F0")
        choice.config(bg = "#1C1C1C", fg = "#F0F0F0")
        choice_entry.config(bg = "#1C1C1C", fg = "#F0F0F0")
        desc.config(bg = "#1C1C1C", fg = "#F0F0F0")
        hours_entry.config(bg = "#1C1C1C", fg = "#F0F0F0")
        minutes_entry.config(bg = "#1C1C1C", fg = "#F0F0F0")
        seconds_entry.config(bg = "#1C1C1C", fg = "#F0F0F0")
    else:           # light
        file.write("0")
        current_theme = 0
        display.config(bg = "#F0F0F0")
        version.config(bg = "#F0F0F0", fg="#000000")
        confirm.config(bg = "#BBF0BB", fg="#000000", activebackground="#BBF0BB", activeforeground="#000000")
        cancel.config(bg = "#FFBBBB", fg="#000000", activebackground="#FFBBBB", activeforeground="#000000")
        theme.config(bg = "#F0F0F0", fg="#000000", activebackground="#F0F0F0", activeforeground="#000000")
        choice.config(bg = "#F0F0F0", fg="#000000")
        choice_entry.config(bg = "#F0F0F0", fg="#000000")
        desc.config(bg = "#F0F0F0", fg="#000000")
        hours_entry.config(bg = "#F0F0F0", fg="#000000")
        minutes_entry.config(bg = "#F0F0F0", fg="#000000")
        seconds_entry.config(bg = "#F0F0F0", fg="#000000")

settings = open(r"shutdown/.settings", "r")
current_theme = int(settings.read())
settings.close()

if(current_theme):           # dark theme
    display.configure(bg = "#1C1C1C")
    version = tk.Label(text="Version 1.1                                                alba4k", bg = "#1C1C1C", fg = "#F0F0F0")
    version.place(x=6,y=307)
    confirm = tk.Button(text="CONFIRM",
        command=_confirm,
        width=8, height=1,
        bg="#116611", fg="#F0F0F0",
        activebackground = "#116611", activeforeground="#F0F0F0")
    confirm.place(x=100,y=260)
    cancel = tk.Button(text="CANCEL",
        command=lambda:os.system("shutdown -a"),
        width=8,height=1,
        bg="#661111", fg="#F0F0F0",
        activebackground = "#661111", activeforeground="#F0F0F0")
    cancel.place(x=100,y=295)
    theme = tk.Button(text="Theme",
        command=theme_check,
        bg = "#1F1F1F", fg = "#F0F0F0",
        activebackground = "#1F1F1F", activeforeground="#F0F0F0")
    theme.place(x=200, y=280)
    choice = tk.Label(text="Type here what you want to do:\n    - shutdown\n    - restart\n    - disconnect -",
        bg = "#1C1C1C", fg = "#F0F0F0")
    choice.place(x=40,y=4)
    choice_entry = tk.Entry(textvar=command, bg = "#1C1C1C", fg = "#F0F0F0")
    choice_entry.place(x=70,y=72)
    desc = tk.Label(text="             hours\n\n\n             minutes\n\n\n             seconds", bg = "#1C1C1C", fg = "#F0F0F0",
        font=("roboto",10, "bold"))
    desc.place(x=50,y=110)
    hours_entry = tk.Entry(textvar=hours, bg = "#1C1C1C", fg = "#F0F0F0")
    hours_entry.place(x=70,y=131)
    minutes_entry = tk.Entry(textvar=minutes, bg = "#1C1C1C", fg = "#F0F0F0")
    minutes_entry.place(x=70,y=180)
    seconds_entry = tk.Entry(textvar=seconds, bg = "#1C1C1C", fg = "#F0F0F0")
    seconds_entry.place(x=70,y=228)
else:                           # light theme
    version = tk.Label(text="Version 1.1                                                alba4k")
    version.place(x=6,y=307)
    confirm = tk.Button(text="CONFIRM",
        command=_confirm,
        width=8,height=1,
        bg="#BBF0BB",
        activebackground="#BBF0BB", activeforeground="#000000")
    confirm.place(x=100,y=260)
    cancel = tk.Button(text="CANCEL",
        command=lambda:os.system("shutdown -a"),
        width=8,height=1,
        bg="#FFBBBB",
        activebackground = "#FFBBBB", activeforeground="#000000")
    cancel.place(x=100,y=295)
    theme = tk.Button(text="Theme",
        command=theme_check)
    theme.place(x=200, y=280)
    choice = tk.Label(text="Type here what you want to do:\n    - shutdown -\n    - restart -\n    - disconnect -")
    choice.place(x=40,y=4)
    choice_entry = tk.Entry(textvar=command)
    choice_entry.place(x=70,y=72)
    desc = tk.Label(text="             hours\n\n\n             minutes\n\n\n             seconds",
        font=("roboto",10, "bold"))
    desc.place(x=50,y=110)
    hours_entry = tk.Entry(textvar=hours)
    hours_entry.place(x=70,y=131)
    minutes_entry = tk.Entry(textvar=minutes)
    minutes_entry.place(x=70,y=180)
    seconds_entry = tk.Entry(textvar=seconds)
    seconds_entry.place(x=70,y=228)
display.mainloop()
