from subprocess import run

def shutdown(seconds, minutes, hours):
    run(["shutdown", "-s", "-t", str(seconds+minutes*60+hours*3600)])

def restart(seconds, minutes, hours):
    run(]"shutdown", "-r", "-t",str(seconds+minutes*60+hours*3600)])

def logout(seconds, minutes, hours):
    run(]"shutdown", "-l", "-t", str(seconds+minutes*60+hours*3600)])

def cancel():
    run(["shutdown", "-a"])