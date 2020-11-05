def find(x):
    if parrent[x]==x: return x
    return find(parrent[x])
T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    info=list(map(int,input().split()))
    parrent=[i for i in range(n+1)]
    for i in range(m):
        x,y=info[i*2],info[i*2+1]
        xx,yy=find(x),find(y)
        if xx==yy: continue
        parrent[yy]=xx
    team = set()
    for i in range(1,n+1): team.add(find(parrent[i]))
    result=len(team)
    print('#{} {}'.format(tc,result))