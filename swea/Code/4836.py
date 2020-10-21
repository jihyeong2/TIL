import sys
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    maps=[[0]*10 for _ in range(10)]
    result=0
    for i in range(n):
        for a in range(arr[i][0],arr[i][2]+1):
            for b in range(arr[i][1],arr[i][3]+1):
                maps[a][b]+=arr[i][4]
                if maps[a][b]>=3: result+=1
    print(f'#{tc} {result}')