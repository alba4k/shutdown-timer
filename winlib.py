from os import system

def shutdown(seconds, minutes, hours):
    system("shutdown -s -t "+str(seconds+minutes*60+hours*3600))

def restart(seconds, minutes, hours):
    system("shutdown -r -t "+str(seconds+minutes*60+hours*3600))

def logout(seconds, minutes, hours):
    system("shutdown -l -t "+str(seconds+minutes*60+hours*3600))

def cancel():
    system("shutdown -a")