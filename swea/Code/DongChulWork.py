# def perm(z,max_r):
#     global result
#     if max_r<=result : return
#     if z==n:
#         result=max(max_r,result)
#     else:
#         for i in range(n):
#             if visit[i]: continue
#             visit[i]=1
#             perm(z+1,max_r*p[z][i]*0.01)
#             visit[i]=0
# T=int(input())
# for tc in range(1,T+1):
#     n=int(input())
#     p=[list(map(int, input().split())) for _ in range(n)]
#     visit,result=[0]*n,0
#     perm(0,100)
#     print('#{} {}'.format(tc,'%0.6f'%result))

#
# for t in range(int(input())):
#     n = int(input())
#     p = [[*map(lambda x: x / 100, map(int, input().split()))] for _ in range(n)]
#     d = [0] * (1 << n)
#     d[0] = 1
#     for mask in range(1 << n):
#         x = sum(1 for i in range(n) if mask & (1 << i))
#         for j in range(n):
#             if mask & (1 << j) == 0:
#                 d[mask | (1 << j)] = max(d[mask | (1 << j)], d[mask] * p[x][j])
#
#     print(f'#{t + 1} {d[-1] * 100:.6f}')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    M = 1 << N
    dp = [[0.0 for _ in range(M)] for _ in range(N)]

    G = []
    for i in range(N):
        G.append(list(map(float, input().split())))
        for j in range(N):
            G[i][j] = G[i][j] / 100

    for i in range(N):
        dp[0][1 << i] = G[0][i]

    for i in range(1, N):
        for cur in range(1, M):
            if dp[i - 1][cur] == 0:
                continue

            for j in range(N):
                if cur & (1 << j) != 0 or G[i][j] == 0:
                    continue
                next = cur | (1 << j)

                dp[i][next] = max(dp[i][next], dp[i - 1][cur] * G[i][j])
    print("#%d %.6f" % (test_case, dp[N - 1][M - 1] * 100))
