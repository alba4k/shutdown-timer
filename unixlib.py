from os import system
from math import ceil

def shutdown(seconds, minutes, hours):
    system("shutdown +" + str(ceil(seconds/60)+minutes+hours*60))

def restart(seconds, minutes, hours):
    system("shutdown -r +" + str(ceil(seconds/60)+minutes+hours*60))

def logout(seconds, minutes, hours):
    system("shutdown -H +" + str(ceil(seconds/60)+minutes+hours*60))

def cancel():
    system("shutdown -c")