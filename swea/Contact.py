import sys
sys.stdin=open("input.txt","r")
def bfs(s,graph):
    q=[[s,0]]
    visit=[0]*101
    visit[s]=1
    maxNum,maxDist=-1,-1
    while q:
        curr,dist=q.pop(0)
        for next in graph[curr]:
            if visit[next]:continue
            visit[next]=1
            q.append([next,dist+1])
        if dist>maxDist:
            maxNum,maxDist=curr,dist
        elif dist==maxDist and curr>maxNum:
            maxNum=curr
        else: continue
    return maxNum

for tc in range(1,11):
    n,s=map(int, input().split())
    arr=list(map(int, input().split()))
    graph=[[] for _ in range(101)]
    for i in range(0,n,2):
        x,y=arr[i],arr[i+1]
        if y not in graph[x]:
            graph[x].append(y)
    result=bfs(s,graph)
    print('#{} {}'.format(tc,result))