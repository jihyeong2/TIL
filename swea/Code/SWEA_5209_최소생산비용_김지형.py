# def dfs(z,res):
#     global result
#     if res>result: return
#     if z==n:
#         result=min(res,result)
#     else:
#         for i in range(n):
#             if visit[i]: continue
#             visit[i]=1
#             dfs(z+1,res+arr[z][i])
#             visit[i]=0
# T=int(input())
# for tc in range(1,T+1):
#     n=int(input())
#     arr=[list(map(int,input().split())) for _ in range(n)]
#     result,visit=float('inf'),[0]*n
#     dfs(0,0)
#     print('#{} {}'.format(tc,result))
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    m=1<<n
    arr=[list(map(int,input().split())) for _ in range(n)]
    dp=[[float('inf')]*m for _ in range(n)]
    for i in range(n):
        dp[0][1<<i]=arr[0][i]
    for i in range(1,n):
        for j in range(1,m):
            if dp[i-1][j]==float('inf') : continue
            for k in range(n):
                if j & (1<<k) == 0 :
                    dp[i][j|1<<k]=min(dp[i][j|1<<k],dp[i-1][j]+arr[i][k])
    print('#{} {}'.format(tc,dp[n-1][m-1]))