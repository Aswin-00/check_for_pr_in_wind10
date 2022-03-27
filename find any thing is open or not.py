import subprocess
import win32ui
def present(st):
    st=st+'.exe'
    st=str(st)
    s=subprocess.check_output("tasklist",shell=True)
    p=(st).encode("utf-8")
    #if p in s:print("yes")
    if(s.find(p)>0):
        print("yes")
    else:
        print("no")
x=input("enter your programe:- ")
present(x)
