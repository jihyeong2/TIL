import sys
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    str1=input()
    str2=input()
    n,m,result=len(str1),len(str2),0
    for i in range(m-n+1):
        if str2[i:i+n]==str1:
            result=1
            break
    print('#{} {}'.format(tc,result))