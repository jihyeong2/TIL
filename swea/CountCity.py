import sys
sys.stdin=open("input.txt","r")
def dfs(x,graph,visit):
    visit[x]=1
    for next in graph[x]:
        if visit[next]: continue
        dfs(next,graph,visit)
T=int(input())
for tc in range(1,T+1):
    n,m=map(int, input().split())
    graph=[[] for _ in range(n+1)]
    visit=[0]*(n+1)
    for _ in range(m):
        x,y=map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    result=0
    for i in range(1,n+1):
        if visit[i]: continue
        dfs(i,graph,visit)
        result+=1
    print('#{} {}'.format(tc,result))