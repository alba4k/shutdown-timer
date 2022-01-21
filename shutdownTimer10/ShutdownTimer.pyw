import tkinter as tk, os
display=tk.Tk()
display.title("Shutdown - alba4k")
display.geometry("250x330")
order,hours,minutes,seconds=tk.StringVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()
def confirm():
    time=str(seconds.get()+minutes.get()*60+hours.get()*3600)
    if order.get()=="shutdown":
        os.system("shutdown /s /t "+time)
    elif order.get()=="restart":
        os.system("shutdown /r /t "+time)
    elif order.get()=="disconnect":
        os.system("shutdown /l")
def cancel():
    os.system("shutdown -a")
confirm_button=tk.Button(display,text="CONFIRM",command=confirm,width=8,height=1).place(x=100,y=260)
cancel_button=tk.Button(display,text="CANCEL",command=cancel,width=8,height=1).place(x=100,y=295)
type_label=tk.Label(display,text="Type here what you want to do:\n    - shutdown\n    - restart\n    - disconnect (no timer)").place(x=40,y=2)
type_entry=tk.Entry(display,textvar=order).place(x=70,y=70)
time_label=tk.Label(display, text="             hours\n\n\n             minutes\n\n\n             seconds").place(x=70,y=112)
hours_entry=tk.Entry(display,textvar=hours).place(x=70,y=135)
minutes_entry=tk.Entry(display,textvar=minutes).place(x=70,y=180)
seconds_entry=tk.Entry(display,textvar=seconds).place(x=70,y=225)
copyright=tk.Label(display,text="alba4k").place(x=200,y=310)
display.mainloop()