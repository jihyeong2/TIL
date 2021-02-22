from sys import stdin
dp=[[[-1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a>20 or b>20 or c>20 :
        return dp[20][20][20] if dp[20][20][20]!=-1 else w(20,20,20)
    dp[a][b][c]=0
    if a<b<c:
        dp[a][b][c]+=dp[a][b][c-1] if dp[a][b][c-1]!=-1 else w(a,b,c-1)
        dp[a][b][c]+=dp[a][b-1][c-1] if dp[a][b-1][c-1]!=-1 else w(a,b-1,c-1)
        dp[a][b][c]-=dp[a][b-1][c] if dp[a][b-1][c]!=-1 else w(a,b-1,c)
    else:
        dp[a][b][c]+=dp[a-1][b][c] if dp[a-1][b][c]!=-1 else w(a-1,b,c)
        dp[a][b][c]+=dp[a-1][b-1][c] if dp[a-1][b-1][c]!=-1 else w(a-1,b-1,c)
        dp[a][b][c]+=dp[a-1][b][c-1] if dp[a-1][b][c-1]!=-1 else w(a-1,b,c-1)
        dp[a][b][c]-=dp[a-1][b-1][c-1] if dp[a-1][b-1][c-1]!=-1 else w(a-1,b-1,c-1)

    return dp[a][b][c]
result=''
while(True):
    a,b,c=map(int, stdin.readline().split())
    if a==-1 and b==-1 and c==-1: break
    result+='w({}, {}, {}) = {}'.format(a,b,c,w(a,b,c)) + '\n'
print(result)