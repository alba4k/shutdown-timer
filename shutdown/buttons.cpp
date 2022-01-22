/*
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
*/

#include <iostream>

void shutdown(int seconds, int minutes, int hours) {
    std::cout << seconds/60 + minutes + hours*60;
}

int main() {
    shutdown(1, 3, 2);
}