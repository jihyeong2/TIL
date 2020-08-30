import sys
sys.stdin=open("input.txt","r")
def dfs(s,g,node,visit):
    res=0
    if s==g: return 1
    for v in node[s]:
        if v in visit: continue
        visit.add(v)
        res+=dfs(v,g,node,visit)
    return res
T=int(input())
for tc in range(1,T+1):
    v,e=map(int,input().split())
    node=[[] for _ in range(v+1)]
    for i in range(e):
        start,end=map(int, input().split())
        node[start].append(end)
    s,g=map(int, input().split())
    visit=set()
    visit.add(s)
    print('#{} {}'.format(tc, dfs(s,g,node,visit)))