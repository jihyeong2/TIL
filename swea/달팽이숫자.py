import sys
sys.stdin=open("input.txt","r")
dx=[0,1,0,-1]
dy=[1,0,-1,0]
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[[0]*n for _ in range(n)]
    num,dir,x,y=1,0,0,-1
    while(num<=n*n):
        nx,ny=x+dx[dir],y+dy[dir]
        if nx<0 or ny<0 or nx>=n or ny>=n or arr[nx][ny]!=0:
            dir=(dir+1)%4
            nx, ny = x + dx[dir], y + dy[dir]
        x,y=nx,ny
        arr[x][y]=num
        num+=1
    print('#{}'.format(tc))
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()