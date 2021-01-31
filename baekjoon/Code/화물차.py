from collections import deque
def bfs():
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    q = deque()
    q.append((sx, sy))
    visit[sx][sy] = True
    t=0
    while q:
        size=len(q)
        t+=1
        while size:
            x, y = q.popleft()
            for dir in range(4):
                nx,ny=x+dx[dir], y+dy[dir]
                if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                    if maps[nx][ny]=='.': continue
                    elif maps[nx][ny]=='#':
                        visit[nx][ny]=True
                        q.append((nx,ny))
                    elif "0"<=maps[nx][ny]<="9":
                        num=int(maps[nx][ny])
                        if 0<=dir<=1:
                            if intersections[num]['dir'] == '|':
                                visit[nx][ny]=True
                                q.append((nx,ny))
                            else:
                                q.append((x,y))
                        else:
                            if intersections[num]['dir'] == '-':
                                visit[nx][ny]=True
                                q.append((nx,ny))
                            else:
                                q.append((x,y))
                    else:
                        # 도착
                        return t
            size-=1

        for i in range(10):
            if intersections[i]==False: continue
            if intersections[i]['dir']=='-':
                if t>=intersections[i]['a']:
                    intersections[i]['a']+=intersections[i]['sum']
                    intersections[i]['dir']='|'
            else:
                if t>=intersections[i]['b']:
                    intersections[i]['b']+=intersections[i]['sum']
                    intersections[i]['dir']='-'

    return "impossible"

while True:
    n,m=map(int, input().split())
    if n==0 and m==0: break
    maps=[]
    intersection_cnt=0
    sx,sy,ex,ey=-1,-1,-1,-1
    for i in range(n):
        tmp=list(input())
        for j in range(m):
            if tmp[j]=='A':
                sx,sy=i,j
            elif tmp[j]=='B':
                ex,ey=i,j
            elif "0"<=tmp[j]<="9":
                intersection_cnt+=1
        maps.append(tmp)
    intersections=[False for _ in range(10)]
    for _ in range(intersection_cnt):
        tmp=input().split()
        intersections[int(tmp[0])]={'dir': tmp[1], 'a': int(tmp[2]), 'b': int(tmp[3])+int(tmp[2]),'sum':int(tmp[3])+int(tmp[2])} if tmp[1]=='-' else {'dir': tmp[1], 'a': int(tmp[2])+int(tmp[3]), 'b': int(tmp[3]),'sum':int(tmp[3])+int(tmp[2])}
    visit=[[False for _ in range(m)] for _ in range(n)]
    print(bfs())
    enter=input()