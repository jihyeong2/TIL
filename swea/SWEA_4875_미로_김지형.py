import sys
sys.stdin=open("input.txt","r")
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def miro(s,maps):
    visit=set()
    while s:
        x, y, flag = s[-1][0],s[-1][1], 0
        visit.add((x,y))
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or (nx,ny) in visit: continue
            if maps[nx][ny]=='1' or maps[nx][ny]=='2': continue
            elif maps[nx][ny] == '3':
                return 1
            else:
                flag = 1
                s.append([nx,ny])
        if not flag: s.pop(-1)
    return 0

T=int(input())
for tc in range(1,T+1):
    n,maps,s=int(input()),[],[]
    for i in range(n):
        temp=list(input())
        for j in range(n):
            if temp[j]=='2': s.append([i,j])
        maps.append(temp)
    result=miro(s,maps)
    print('#{} {}'.format(tc,result))
