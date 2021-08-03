def check(x,y):
    for j in x:
        if(j in y and x.count(j)==y.count(j)):
            print("YES")
            break
        else:
            print("NO")
            break
n=int(input())
for i in range(n):
    s=input()
    s1=''
    s2=''
    if(len(s)%2!=0):
        s1=s[0:len(s)//2+1]
        s2=s[len(s)//2:]
    else:
        s1=s[0:len(s)//2-1]
        s2=s[len(s)//2:]
    check(s1,s2)
    
