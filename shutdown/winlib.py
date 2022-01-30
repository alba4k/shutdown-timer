import os

def shutdown(seconds, minutes, hours):
    os.system("shutdown -s -t "+str(seconds+minutes*60+hours*3600))

def restart(seconds, minutes, hours):
os.system("shutdown -r -t "+str(seconds+minutes*60+hours*3600))

def logout(seconds, minutes, hours):
    os.system("shutdown -l -t "+str(seconds+minutes*60+hours*3600))

def cancel():
    os.system("shutdown -a")
