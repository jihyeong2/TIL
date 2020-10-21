import sys
sys.stdin=open("input.txt","r")
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(1,11):
    n=int(input())
    maps=list()
    for _ in range(16):
        num=input()
        temp=list()
        for i in range(16):
            temp.append(int(num[i]))
        maps.append(temp)
    s=list()
    s.append([1,1])
    result=0
    while s:
        flag=0
        x,y=s[len(s)-1][0],s[len(s)-1][1]
        if maps[x][y]==0: maps[x][y]=1
        if maps[x][y]==3:
            result=1
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if maps[nx][ny]==1 or maps[nx][ny]==2:continue
            flag=1
            s.append([nx,ny])
        if flag==0:
            s.pop()
    print(f'#{n} {result}')