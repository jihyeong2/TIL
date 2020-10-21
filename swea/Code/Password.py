import sys
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    n,k=map(int,input().split())
    password_str=input()
    passwords=list()
    result=list()
    for password in password_str:
        if ord('A')<=ord(password)<=ord('F'):
            passwords.append(ord(password)-ord('A')+10)
        else:
            passwords.append(int(password))
    for i in range(n//4):
        for j in range(0,n,n//4):
            sum=0
            for l in range(n//4):
                idx = -i+j+l
                if idx<0 : idx+=n
                sum+=passwords[idx]*(16**(n//4-1-l))
            if sum not in result:
                result.append(sum)
    result.sort()
    result.reverse()
    print(f'#{tc} {result[k-1]}')                