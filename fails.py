#!/usr/bin/python3
def main():
    def read_file():
        with open("name.txt") as f:
            a=f.read().splitlines()
            return a
    rfile=read_file()
    # ind=0
    def sort_names(a):
        b=input("yst inchi eq uzum sortavorel:")
        names=[]
        ind=0
        for i in range(len(a)):
            n=a[i].split()
            if b.lower()=="name":
                ind=0
                names.append(n[ind])
            elif b.lower()=="surname":
                ind=1
                names.append(n[ind])
            elif b.lower()=="age":
                ind=2
                names.append(n[ind])
            elif b.lower()=="proffession":
                ind=3
                names.append(n[ind])
        names.sort()
        return names ,ind
    sname=sort_names(rfile)
    def append_files(a,b,c):
        for i in range(len(b)):
            for j in range(len(a)):
                n=a[j].split()
                if n[c]==b[i]:
                    with open("sorted_file.txt", 'a') as f:
                        f.write(a[j]+"\n")

                    
    append_files(rfile,sname[0],sname[1])
