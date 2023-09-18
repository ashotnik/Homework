#!/usr/bin/python3
import os
import datetime
directory = "tests"
a=os.listdir()
if not directory in a:
    os.mkdir(directory)



i=0
while i<10:
    time=datetime.datetime.now()
    sttime=str(time)
    fail="tests/"+sttime
    with open(fail,'w') as f:
        if int(sttime[-1])%2==0:
            f.write("pass")
        else:
            f.write("error")
    i+=1