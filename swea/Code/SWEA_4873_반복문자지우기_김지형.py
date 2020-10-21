import sys
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    arr=input()
    s=list()
    s.append(arr[0])
    for i in range(1,len(arr)):
        if len(s)==0 or s[-1]!=arr[i]:s.append(arr[i])
        else:
            s.pop()
    print('#{} {}'.format(tc,len(s)))