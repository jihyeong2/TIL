T=int(input())
for tc in range(1,T+1):
    n=int(input())
    num=list(map(int,input().split()))
    print(f'#{tc} {max(num)-min(num)}')