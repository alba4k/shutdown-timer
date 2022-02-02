from json import loads,dumps
import tkinter as tk
from PIL import ImageTk
import PIL._tkinter_finder
import unixlib as buttons
from os import chdir,path

settings_json = open("shutdown/settings.json", "r")
settings = loads(settings_json.read())
settings_json.close()

def lang_check(lang, settings_display = None,theme = None,theme_desc = None, apply = None):
    settings["lang"] = lang
    version.config(text=settings[settings["lang"]]["display.version"]+" 2.0\t\t\t         alba4k")
    if(theme):
        settings_display.title(settings[settings["lang"]]["settings.title"])
        theme.config(text=settings[settings["lang"]]["settings.theme"])
        theme_desc.config(text=settings[settings["lang"]]["settings.theme_desc"])
        apply.config(text=settings[settings["lang"]]["settings.apply"])

def theme_check(theme = None,settings_display = None,theme_desc = None,lang_select=None, apply=None,change_settings = False):
    if(change_settings):   # checks if it should change the settings.json file
        settings["usingDarkTheme"] = not settings["usingDarkTheme"]
    if(settings["usingDarkTheme"]):           # dark theme is on (primary window, display)
        display.config(bg = "#1C1C1C")
        version.config(bg="#1C1C1C", fg="#F0F0F0")
        cancel.config(bg="#1C1C1C", activebackground = "#1C1C1C")
        hours_entry.config(bg = "#252525", fg = "#F0F0F0")
        minutes_entry.config(bg = "#252525", fg = "#F0F0F0")
        seconds_entry.config(bg = "#252525", fg = "#F0F0F0")
        timer_label_1.config(bg = "#1C1C1C", fg = "#F0F0F0")
        timer_label_2.config(bg = "#1C1C1C", fg = "#F0F0F0")
        restart_button.config(bg="#1C1C1C", activebackground = "#1C1C1C")
        shutdown_button.config(bg="#1C1C1C", activebackground = "#1C1C1C")
        logout_button.config(bg="#1C1C1C", activebackground = "#1C1C1C")
        settings_show.config(bg="#1C1C1C", activebackground="#1C1C1C", image = white_settings_icon)

        if(theme):    # Apply dark theme to the secondary window, if shown
            settings_display.config(bg="#1C1C1C")
            theme.config(bg="#272727", fg = "#F0F0F0", activebackground = "#202020", activeforeground="#F0F0F0")
            apply.config(bg="#272727", fg = "#F0F0F0", activebackground = "#202020", activeforeground="#F0F0F0")
            theme_desc.config(bg = "#1c1c1c", fg = "#f0f0f0")
            lang_select.config(bg = "#1c1c1c", fg = "#f0f0f0", activebackground = "#1c1c1c", activeforeground="#F0F0F0", highlightthickness=0)
            lang_select["menu"].config(bg = "#1c1c1c", fg = "#f0f0f0", activebackground = "#222299", activeforeground="#F0F0F0")
    else:    # light theme is on (primary window, display)
        display.config(bg = "#F0F0F0")
        version.config(bg = "#F0F0F0", fg="#000000")
        cancel.config(bg = "#F0F0F0", activebackground="#F0F0F0")
        hours_entry.config(bg = "#DADADA", fg="#000000")
        minutes_entry.config(bg = "#DADADA", fg="#000000")
        seconds_entry.config(bg = "#DADADA", fg="#000000")
        timer_label_1.config(bg = "#F0F0F0", fg = "#000000")
        timer_label_2.config(bg = "#F0F0F0", fg = "#000000")
        restart_button.config(bg="#F0F0F0", activebackground = "#F0F0F0")
        shutdown_button.config(bg="#F0F0F0", activebackground = "#F0F0F0")
        logout_button.config(bg="#F0F0F0", activebackground = "#F0F0F0")
        settings_show.config(bg = "#F0F0F0", activebackground="#F0F0F0", image = black_settings_icon)

        if(theme):    # Apply light theme to the secondary window, if shown
            settings_display.config(bg="#F0F0F0")
            theme.config(bg = "#F0F0F0", fg="#000000", activebackground="#F0F0F0", activeforeground="#000000")
            apply.config(bg = "#F0F0F0", fg="#000000", activebackground="#F0F0F0", activeforeground="#000000")
            theme_desc.config(bg = "#f0f0f0", fg = "#000000")
            lang_select.config(bg = "#f0f0f0", fg = "#000000", activebackground="#f0f0f0", activeforeground="#000000", highlightthickness=0)
            lang_select["menu"].config(bg = "#f0f0f0", fg = "#000000", activebackground="#9999FF", activeforeground="#000000")

def open_settings():
    settings_display = tk.Tk()
    settings_display.geometry("300x200")
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
        command=lambda: lang_check(lang_choice.get(),
            settings_display,
            theme,
            theme_desc,
            apply
        ),
        highlightthickness=0
    )
    apply.place(x=150, y=150)
    theme.place(x=15, y=60)
    theme_check(theme, settings_display, theme_desc, lang_select, apply)
    lang_check(settings["lang"], settings_display, theme, theme_desc, apply)

display=tk.Tk(className="\nShutdown")
display.geometry("400x250")
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
#theme_check()
#lang_check(settings["lang"])

display.mainloop()

settings_json = open("shutdown/settings.json", "w")
settings_json.write(dumps(settings, indent = 4))
settings_json.close()
