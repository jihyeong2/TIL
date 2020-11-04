def calPlace(x,y,xx,yy):
    return abs(x-xx) + abs(y-yy)
# def perm(z,max_r,idx):
#     global result
#     if result<=max_r: return
#     if z==n:
#         max_r+=calPlace(info[-2],info[-1],info[idx*2],info[idx*2+1])
#         result=min(result,max_r)
#     else:
#         for i in range(1,n+1):
#             if visit[i]: continue
#             visit[i]=1
#             perm(z+1,max_r+calPlace(info[idx*2],info[idx*2+1],info[i*2],info[i*2+1]),i)
#             visit[i]=0
# T=int(input())
# for tc in range(1,T+1):
#     n=int(input())
#     info=list(map(int, input().split()))
#     info[2],info[-2]=info[-2],info[2]
#     info[3],info[-1]=info[-1],info[3]
#     result,visit=float('inf'),[0]*(n+2)
#     perm(0,0,0)
#     print('#{} {}'.format(tc,result))

# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     D = [[987654321] * (N + 2) for _ in range(1 << (N + 2))]
#
#     pos = [[arr[0], arr[1]]]
#     for i in range(4, (N + 2) * 2, 2):
#         pos.append([arr[i], arr[i + 1]])
#     pos.append([arr[2], arr[3]])
#
#     G = [[0] * (N + 2) for _ in range(N + 2)]
#
#     for i in range(N + 1):
#         for j in range(i + 1, N + 2):
#             G[i][j] = abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])
#             G[j][i] = G[i][j]
#
#     D[1][0] = 0
#
#     for visit in range(1, 1 << (N + 1)):  # 방문한 정점들 집합
#         for last in range(N + 1):
#             if visit & (1 << last) == 0: continue
#
#             for next in range(1, N + 1):
#                 if last == next or (visit & 1 << next): continue
#                 next_visit = visit | (1 << next)
#                 D[next_visit][next] = min(D[next_visit][next], D[visit][last] + G[last][next])
#
#     visit = (1 << N + 1) - 1
#     ans = 987654321
#
#     for i in range(1, N + 1):
#         ans = min(ans, D[visit][i] + G[i][N + 1])
#
#     print('#{} {}'.format(tc, ans))
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    info=list(map(int,input().split()))
    v=[(info[0],info[1])]
    for i in range(2,n+2):
        v.append((info[i*2],info[i*2+1]))
    v.append((info[2],info[3]))
    m=1<<(n+1)
    T=[[float('inf')]*(n+1) for _ in range(m)]
    T[1][0]=0
    for visit in range(1,m):
        for last in range(n+1):
            if visit & 1<<last == 0: continue
            for next in range(1,n+1):
                if visit & 1<<next : continue
                n_visit=visit | 1<<next
                T[n_visit][next]=min(T[n_visit][next],T[visit][last]+calPlace(v[last][0],v[last][1],v[next][0],v[next][1]))
    result=float('inf')
    for i in range(1,n+1):
        result=min(result,T[m-1][i]+calPlace(v[n+1][0],v[n+1][1],v[i][0],v[i][1]))
    print('#{} {}'.format(tc,result))