import os
import sys

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
