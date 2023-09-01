#!/usr/bin/python3
# mylist=[10,1,3,20,45,50,60,1,6,8,45,54]

# def get_list(ml):
#     mmax=0
    
#     for i in range(len(ml)):
#         cnt=0
#         for j in range(i+1,len(ml)):
#             if len(ml)==j:break
#             if ml[i]>=ml[j]:break
#             cnt+=1
#             a=i
#             b=j+1
#         if cnt>mmax:
#             mmax=cnt
#             biggestlist=ml[a:b]
#     return biggestlist        
# big_list=get_list(mylist) 
# print(big_list)

mathics="(17+38)-(19-17))"
def math_correct(math):
    chk=1
    for i in math:
        if chk==0 and i=="(":
            print(False)
            break
        elif i=="(":
            chk=0
        elif i==")" and chk !=0:
            print(False)
            break
        elif i==")":
            chk=1
    
        
math_correct(mathics)