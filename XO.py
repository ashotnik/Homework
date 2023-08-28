#!/usr/bin/python3
rol=[1,2,3,4,5,6,7,8,9]
def check_winner(check,g):
    win=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[2,5,7],[2,5,8],[1,4,7],[3,6,9]]
    
    for i in win:
        l=0
        for j in i:
            if j in check:
                l+=1
            if l==3:
                print("haxtec: "+g+"-y")
                return 1
def match(a):
    
    f=""
    n=0
    for i in a:
        f+=str(i)+" "
        n+=1
        if n==3:
            n=0
            f+="\n"
    print(f)
    return a

def game(m):
    bool=True
    x=[]
    y=[]
    g="x"
    for i in range(len(m)):
        inp = int(input("nsheq vortex lini "+g+':'))
        if bool:
            g="x"
            bool=False
            x.append(inp)
            check=check_winner(x,'x')
            if check==1:break
        else:
            g="y"
            bool=True
            y.append(inp)
            check=check_winner(y,'y')
            if check==1:break
        for ind in range(len(m)):
            if m[ind]==inp:
                m[ind]=g
                match(m)
def main(a):
    mat=match(a)
    game(mat)
main(rol)