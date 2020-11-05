def find(x):
    if parrent[x]==x: return x
    return find(parrent[x])
T=int(input())
for tc in range(1,T+1):
    v,e=map(int,input().split())
    edge=[]
    for _ in range(e):
        a,b,c=map(int,input().split())
        edge.append((a,b,c))
    parrent=[i for i in range(v+1)]
    edge.sort(key=lambda x : x[2])
    result,cnt,idx=0,0,0
    while cnt<v:
        x,y,dist=edge[idx]
        xx,yy=find(x),find(y)
        if xx==yy:
            idx+=1
            continue
        parrent[yy]=xx
        result+=dist
        cnt+=1
        idx+=1
    print('#{} {}'.format(tc,result))