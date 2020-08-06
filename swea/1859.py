import sys
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=list(map(int,input().split()))
    money=0
    cnt=0
    price=arr[n-1]
    for i in arr[-2::-1]:
        if price<=i:
            money+=cnt*price
            price=i
            cnt=0
        else:
            money-=i
            cnt+=1
        # print(i,price,money,cnt)
    if cnt>0: money+=cnt*price
    result=0
    if money<=0:result=0
    else: result=money
    print(f'#{tc} {result}')