#!/usr/bin/python3
import os
import shutil

def files():
    directory = "/home/ashot/python/parapunq/dir1"
    files = os.listdir(directory)
    return files


def sorting(fil):
    directory = "/home/ashot/python/parapunq/dir1"
    fi=os.listdir(directory)
    for i in fil:
        spl=i.split(".")
        if not spl[-1] in fi:
            path = os.path.join(directory, spl[-1])
            os.mkdir(path)
            shutil.move(directory+"/"+i,directory+'/'+spl[-1])
        else:
            shutil.move(directory+"/"+i,directory+'/'+spl[-1])
def main():
    file =files()
    sorted=sorting(file)
main()