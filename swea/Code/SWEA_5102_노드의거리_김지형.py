import sys
sys.stdin=open("input.txt","r")
def bfs(s,g,v,graph):
    q=[]
    q.append([s,0])
    visit=[0]*(v+1)
    visit[s]=1
    while q:
        curr,cnt=q.pop(0)
        for next in graph[curr]:
            if next==g: return cnt+1
            if not visit[next]:
                visit[next]=1
                q.append([next,cnt+1])
    return 0
T=int(input())
for tc in range(1,T+1):
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    for _ in range(e):
        x,y=map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    s,g=map(int, input().split())
    result=bfs(s,g,v,graph)
    print('#{} {}'.format(tc,result))