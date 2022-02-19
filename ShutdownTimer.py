#!/usr/bin/python

from json import loads,dumps
import tkinter as tk
from PIL import ImageTk
import PIL._tkinter_finder
import unixlib as buttons

settings_json = open("shutdown/config.json", "r")
settings = loads(settings_json.read())
settings_json.close()

def lang_check(settings_display = None,theme = None,theme_desc = None, apply = None, lang = settings["lang"]):
    settings["lang"] = lang
    version.config(text=settings[settings["lang"]]["display.version"]+" 2.0\t\t\t         alba4k")
    if(theme):
        settings_display.title(settings[settings["lang"]]["settings.title"])
        theme.config(text=settings[settings["lang"]]["settings.theme"])
        theme_desc.config(text=settings[settings["lang"]]["settings.theme_desc"])
        apply.config(text=settings[settings["lang"]]["settings.apply"])

def theme_check(theme=None, settings_display=None,theme_desc=None,lang_select=None, apply=None,change_settings = False):
    if(settings["usingDarkTheme"]):
        if(change_settings):
            settings["usingDarkTheme"] = False
            settings["colors"]["bg"] = "#f0f0f0"
            settings["colors"]["fg"] = "#000000"
            settings["colors"]["alt"] = "#dadada"
            settings_show.config(image=black_settings_icon)
        else:
            settings_show.config(image=white_settings_icon)
    elif(change_settings):
        settings["usingDarkTheme"] = True
        settings["colors"]["bg"] = "#1c1c1c"
        settings["colors"]["fg"] = "#f0f0f0"
        settings["colors"]["alt"] = "#252525"
        settings_show.config(image=white_settings_icon)
    else:
        settings_show.config(image=black_settings_icon)


    display.config(bg = settings["colors"]["bg"])
    version.config(bg = settings["colors"]["bg"], fg=settings["colors"]["fg"])
    cancel.config(bg=settings["colors"]["bg"], activebackground = settings["colors"]["bg"])
    hours_entry.config(bg = settings["colors"]["alt"], fg = settings["colors"]["fg"])
    minutes_entry.config(bg = settings["colors"]["alt"], fg = settings["colors"]["fg"])
    seconds_entry.config(bg = settings["colors"]["alt"], fg = settings["colors"]["fg"])
    timer_label_1.config(bg = settings["colors"]["bg"], fg = settings["colors"]["fg"])
    timer_label_2.config(bg = settings["colors"]["bg"], fg = "#F0F0F0")
    restart_button.config(bg=settings["colors"]["bg"], activebackground = settings["colors"]["bg"])
    shutdown_button.config(bg=settings["colors"]["bg"], activebackground = settings["colors"]["bg"])
    logout_button.config(bg=settings["colors"]["bg"], activebackground = settings["colors"]["bg"])
    settings_show.config(bg=settings["colors"]["bg"], activebackground= settings["colors"]["bg"])

    if(theme):    # Apply dark theme to the secondary window, if shown
        settings_display.config(bg = settings["colors"]["bg"])
        theme.config(bg = settings["colors"]["alt"], fg = settings["colors"]["fg"], activebackground = settings["colors"]["bg"], activeforeground=settings["colors"]["fg"])
        apply.config(bg = settings["colors"]["alt"], fg = settings["colors"]["fg"], activebackground = settings["colors"]["bg"], activeforeground=settings["colors"]["fg"])
        theme_desc.config(bg = settings["colors"]["bg"], fg = settings["colors"]["fg"])
        lang_select.config(bg = settings["colors"]["bg"], fg = settings["colors"]["fg"], activebackground = settings["colors"]["bg"], activeforeground=settings["colors"]["fg"], highlightthickness=0)
        lang_select["menu"].config(bg = settings["colors"]["bg"], fg = settings["colors"]["fg"], activebackground = settings["colors"]["select"], activeforeground=settings["colors"]["fg"])
   
def open_settings():
    settings_display = tk.Tk()
    settings_display.geometry("300x200")
    settings_display.resizable(False, False)
    lang_choice = tk.StringVar(settings_display)
    lang_choice.set(settings["lang"])
   
    lang_select = tk.OptionMenu(settings_display,
        lang_choice,
        *["English", "Italian", "Spanish", "French"]
    )
    lang_select.place(x=15, y=15)

    theme_desc = tk.Label(settings_display,
        font = ("Helvetica, 12"),
        highlightthickness=0
    )
    theme_desc.place(x=90, y=55)

    theme = tk.Button(settings_display,
        command=lambda: theme_check(theme,
            settings_display,
            theme_desc,
            lang_select,
            apply,
            True
        ),
        highlightthickness=0
    )

    apply = tk.Button(settings_display,
        command=lambda: lang_check(settings_display,
            theme,
            theme_desc,
            apply,
            lang_choice.get()
        ),
        highlightthickness=0
    )
    apply.place(x=150, y=150)
    theme.place(x=15, y=60)
    theme_check(theme, settings_display, theme_desc, lang_select, apply)
    lang_check(settings_display, theme, theme_desc, apply)

display=tk.Tk(className=" Shutdown")
display.geometry("400x250")
display.resizable(False, False)
#display.iconbitmap("shutdown/assets/icon.ico")
hours,minutes,seconds=tk.IntVar(),tk.IntVar(),tk.IntVar()

shutdown_icon = ImageTk.PhotoImage(file="shutdown/assets/icons/shutdown.png")
restart_icon = ImageTk.PhotoImage(file="shutdown/assets/icons/restart.png")
logout_icon = ImageTk.PhotoImage(file="shutdown/assets/icons/logout.png")
cancel_icon = ImageTk.PhotoImage(file="shutdown/assets/icons/cancel.png")
white_settings_icon = ImageTk.PhotoImage(file="shutdown/assets/icons/white_settings.png")
black_settings_icon = ImageTk.PhotoImage(file="shutdown/assets/icons/black_settings.png")

version = tk.Label(display,
    font=("Helvetica", 12))
version.place(x = 12, y = 220)

shutdown_button = tk.Button(display,
    image = shutdown_icon,
    command=lambda: buttons.shutdown(seconds.get(), minutes.get(), hours.get()),
    borderwidth=0,
    highlightthickness=0
)
shutdown_button.place(x=50,y=150)

restart_button = tk.Button(display,
    image = restart_icon,
    command=lambda: buttons.restart(seconds.get(), minutes.get(), hours.get()),
    borderwidth=0,
    highlightthickness=0
)
restart_button.place(x=125,y=150)

logout_button = tk.Button(display,
    image = logout_icon,
    command=lambda: buttons.logout(seconds.get(), minutes.get(), hours.get),
    borderwidth=0,
    highlightthickness=0
)
logout_button.place(x=200,y=150)

cancel = tk.Button(display,
    image = cancel_icon,
    command=buttons.cancel,
    borderwidth=0,
    highlightthickness=0
)
cancel.place(x=300,y=150)

settings_show = tk.Button(display,
    command=open_settings,
    borderwidth=0,
    highlightthickness=0
)
settings_show.place(x=300, y=50)

timer_label_1 = tk.Label(display,
    text=":",
    font=("Calibri", 25, "bold")
)
timer_label_1.place(x=103, y=50)
timer_label_2 = tk.Label(display,
    text=":",
    font=("Calibri", 25, "bold")
)
timer_label_2.place(x=179, y=50)

hours_entry = tk.Entry(display,
    textvar=hours,
    font=("Helvetica", 30, "bold"))
hours_entry.place(x=50, y=50, width=50, height=50)

minutes_entry = tk.Entry(display,
    textvar=minutes,
    font=("Helvetica", 30, "bold"))
minutes_entry.place(x=125, y=50, width=50, height=50)

seconds_entry = tk.Entry(display,
    textvar=seconds,
    font=("Helvetica", 30, "bold"))
seconds_entry.place(x=200, y=50, width=50, height=50)

open_settings() #when testing in the secondary window
theme_check()
lang_check()

display.mainloop()

settings_json = open("shutdown/config.json", "w")
settings_json.write(dumps(settings, indent = 4))
settings_json.close()