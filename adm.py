#!/usr/bin/python3
def adm():
    while True:
        harc=input("mutqagreq harcy aranc harcakani: ")
        check_qu=check_question(harc)
        if check_qu:
            pat=input("mutqagreq chisht patasxany: ")
            sxal1=input("mutqagreq sxal patasxannery: ")
            sxal2=input("mutqagreq sxal patasxannery: ")
            sxal3=input("mutqagreq sxal patasxannery: ")
            ml=harc+"?"+pat+","+sxal1+","+sxal2+","+sxal3
            return ml
        else:
             print("Harcy goyutyun uni")
             chk=check()
             if chk==False:return False

def append(question):
    with open("as.txt","a") as f:
            f.write("\n"+question)

def check_question(questions):
    with open("as.txt") as f:
            qu=f.readlines()
            for i in qu:
                x=i.split("?")
                if x[0]==questions:
                     return False
            return True

def check():
    inp=input("uzumeq mutqagrel harc?Yes|No ")
    if inp.lower()=="no":
        return False

def main():
    while True:
        ch=check()
        if ch==False:break    
        harc=adm()
        if harc==False:break   
        append(harc)
main()