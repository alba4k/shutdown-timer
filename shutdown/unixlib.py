import os
import math

def shutdown(seconds, minutes, hours):
    os.system("shutdown +" + str(ceil(seconds/60)+minutes+hours*60))

def restart(seconds, minutes, hours):
    os.system("shutdown -r +" + str(ceil(seconds/60)+minutes+hours*60))

def logout(seconds, minutes, hours):
    os.system("shutdown -H +" + str(ceil(seconds/60)+minutes+hours*60))

def cancel():
    os.system("shutdown -c")