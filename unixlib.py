from subprocess import run
from math import ceil

def shutdown(seconds, minutes, hours):
    run(["shutdown", str(ceil(seconds/60)+minutes+hours*60)])

def restart(seconds, minutes, hours):
    run(["shutdown", "-r", str(ceil(seconds/60)+minutes+hours*60)])

def logout(seconds, minutes, hours):
    run(["sudo shutdown", "-H", str(ceil(seconds/60)+minutes+hours*60)])

def cancel():
    run(["shutdown", "-c"])