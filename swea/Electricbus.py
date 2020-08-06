t = int(input())
for tc in range(1, t+1):
    k,n,m=map(int, input().split())
    add = list(map(int, input().split()))
    place=0
    result=0
    while True :
        cnt=0
        for i in range(place+k+1)[::-1]:
            if i in add:
                place=i
                break
            cnt+=1
        if cnt>=k:
            result=0
            break
        else:
            result+=1
        if place+k>=n:
            break
    print(f'#{tc} {result}')
