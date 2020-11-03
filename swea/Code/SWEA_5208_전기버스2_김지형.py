def dfs(idx,cnt):
    global result
    if cnt>result: return
    if idx>=n-1:
        result=min(result,cnt)
    else:
        for i in range(bat[idx],0,-1):
            n_idx=idx+i
            dfs(n_idx,cnt+1)
T=int(input())
for tc in range(1,T+1):
    info=list(map(int, input().split()))
    n,bat=info[0],info[1:]
    result=float('inf')
    dfs(0,-1)
    print('#{} {}'.format(tc,result))