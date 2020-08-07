import sys
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    print(f'#{tc}')
    for i in range(n):
        result1,result2,result3='','',''
        for j in range(n):
            result1+=str(arr[n-1-j][i])
            result2+=str(arr[n-1-i][n-1-j])
            result3+=str(arr[j][n-1-i])
        print(result1,result2,result3)