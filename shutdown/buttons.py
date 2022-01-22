import os
import sys
"""
if sys.platform == "win32":
    def shutdown(seconds, minutes, hours):
        os.system("shutdown -s -t "+str(seconds+minutes*60+hours*3600))
    def restart(seconds, minutes, hours):
        os.system("shutdown -r -t "+str(seconds+minutes*60+hours*3600))
    def logout(seconds, minutes, hours):
        os.system("shutdown -l")
    def cancel():
        os.system("shutdown -a")

if sys.platform == ("darwin" or "linux" or "linux2"):
    def shutdown(seconds, minutes, hours):
        os.system("sleep " + str(seconds+minutes*60+hours+3600) + " && poweroff")
    def restart(seconds, minutes, hours):
        os.system("sleep " + str(seconds+minutes*60+hours+3600) + " && reboot")
    def logout(seconds, minutes, hours):
        os.system("sleep " + str(seconds+minutes*60+hours+3600) + " && logout")
    def cancel():
        os.system("shutdown -c")
"""

def shutdown(seconds, minutes, hours):
    if(sys.platform == "win32"):
        os.system("shutdown -s -t "+str(seconds+minutes*60+hours*3600))
    else:
        os.system("shutdown +" + str(int(seconds/60)+minutes+hours*60+(seconds/60>0)))
def restart(seconds, minutes, hours):
    if(sys.platform == "win32"):
        os.system("shutdown -r -t "+str(seconds+minutes*60+hours*3600))
    else:
        os.system("shutdown -r +" + str(int(seconds/60)+minutes+hours*60+(seconds/60>0)))
def logout(seconds, minutes, hours):
    if(sys.platform == "win32"):
        os.system("shutdown -l -t "+str(seconds+minutes*60+hours*3600))
    else:
        os.system("shutdown -H +" + str(int(seconds/60)+minutes+hours*60+(seconds/60>0)))
def cancel():
    if(sys.platform == "win32"):
        os.system("shutdown -a")
    else:
        os.system("shutdown -c")