import sys
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]
    dp=[[0]*n for _ in range(n)]
    dp[0][0]=arr[0][0]
    for i in range(1,n):
        dp[0][i]=arr[0][i]+dp[0][i-1]
        dp[i][0]=arr[i][0]+dp[i-1][0]
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j]=min(dp[i-1][j]+arr[i][j],dp[i][j-1]+arr[i][j])
    print('#{} {}'.format(tc,dp[n-1][n-1]))