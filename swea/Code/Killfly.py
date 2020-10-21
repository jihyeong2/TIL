import sys
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]
    result=0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum=0
            for a in range(m):
                for b in range(m):
                    sum+=arr[i+a][j+b]
            result=max(result,sum)
    print(f'#{tc} {result}')