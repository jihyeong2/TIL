import sys
sys.stdin=open("input.txt","r")
T=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dfs(a,b,x,y,arr,visit,sub_mat):
    sub_mat[len(sub_mat)-1][0]=max(sub_mat[len(sub_mat)-1][0],x-a+1)
    sub_mat[len(sub_mat)-1][1]=max(sub_mat[len(sub_mat)-1][1],y-b+1)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n: continue
        if arr[nx][ny]==0 or visit[nx][ny]: continue
        visit[nx][ny] = 1
        dfs(a,b,nx,ny,arr,visit,sub_mat)
for tc in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    visit=[[0]*n for _ in range(n)]
    sub_mat=list()
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0 or visit[i][j]:continue
            sub_mat.append([0,0])
            visit[i][j]=1
            dfs(i,j,i,j,arr,visit,sub_mat)
    sub_mat=sorted(sub_mat,key=lambda x : (x[0]*x[1],x[0]))
    print(f'#{tc} {len(sub_mat)}',end=' ')
    for mat in sub_mat:
        print(mat[0],mat[1],end=' ')
    print()