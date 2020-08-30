T=int(input())
for tc in range(1,T+1):
    n=int(input())
    n//=10
    dp=[0]*(n+1)
    dp[1],dp[2]=1,3
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]*2
    print('#{} {}'.format(tc,dp[n]))