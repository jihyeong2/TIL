import sys
sys.stdin=open("input.txt","r")
# def dfs(node,r_graph,result):
#     for r_node in r_graph[node]:
#         if r_node in result: continue
#         dfs(r_node,r_graph,result)
#     result.append(node)
# for tc in range(1,13):
#     v,e=map(int,input().split())
#     node=list(map(int, input().split()))
#     r_graph=[[] for _ in range(v+1)]
#     result=[]
#     for i in range(0,len(node),2):
#         r_graph[node[i+1]].append(node[i])
#     for i in range(1,v+1):
#         if i in result: continue
#         dfs(i,r_graph,result)
#     print('#{}'.format(tc),end=' ')
#     for node in result:
#         print(node,end=' ')
#     print()

def BFS(v):
    q = [v]
    ans = [v]  # 임시로 v를 담을 리스트
    visited[v] = True
    # print(v,'v',end = ' ')
    while q:
        pv = q.pop(0)
        # w를 돌면서 pv와 연결된 것이 있는지 찾는다
        size=len(q)
        for w in range(1, V + 1):
            # w가 pv와 연결된 것이 있는데 만약 w에 방문을 하지 않았다면 w를 q에 넣어줌
            if G[w][pv] == 1:
                # 그 이전의 정점이 방문하지 않았다면
                if visited[w] == False:
                    visited[w] = True
                    q.append(w)
        # q에 담긴 가지 않았던 정점들을 ans에 추가해줌
        if len(q)>size:
            ans += q
    # ans는 뒷 순서부터 담겼기 때문에 뒤집어줌
    ans = ans[::-1]
    # ans에 마지막으로 연결된 v를 담아줌
    return ans


for tc in range(1, 2):
    # 정점의 총 V와 간선의 총 수 E가 주어짐
    V, E = map(int, input().split())
    # 인접행렬
    G = [[0] * (V + 1) for _ in range(V + 1)]
    temp = list(map(int, input().split()))
    # print(temp)
    visited = [False for _ in range(V + 1)]
    for i in range(0, len(temp), 2):
        st, ed = temp[i], temp[i + 1]
        # print(st,ed)
        G[st][ed] = 1
        # G[ed][st] = 1
    result = []
    for i in range(1, V + 1):
        if visited[i] == False:
            result.extend(BFS(i))

    print('#{}'.format(tc), end=' ')
    for r in result:
        print(r, end=' ')
    print()