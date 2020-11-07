from collections import deque
def bfs():
    q = deque()
    q.append((n, 0))
    check = {}
    while q:
        x, cnt = q.popleft()
        if check.get(x, 0): continue
        check[x] = 1
        if x == m: return cnt
        cnt += 1
        if 0 < x + 1 <= 1000000:
            q.append((x + 1, cnt))
        if 0 < x - 1 <= 1000000:
            q.append((x - 1, cnt))
        if 0 < x * 2 <= 1000000:
            q.append((x * 2, cnt))
        if 0 < x - 10 <= 1000000:
            q.append((x - 10, cnt))

T=int(input())
for tc in range(1,T+1):
    n,m = map(int, input().split())
    result=bfs()
    print('#{} {}'.format(tc, result))