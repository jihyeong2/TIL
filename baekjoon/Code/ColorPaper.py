arr=[list(map(int, input().split())) for _ in range(10)]
paper=[[0]*10 for _ in range(10)]
paper_state=[0,5,5,5,5,5]
paper_pos=[]
for i in range(10):
    for j in range(10):
        if arr[i][j]==1: paper_pos.append((i,j))
result=25
def square(x,y,dist,position):
    for i in range(x,x+dist):
        for j in range(y,y+dist):
            if i<0 or j<0 or i>=10 or j>=10 : return False
            if arr[i][j]!=1: return False
            if paper[i][j]!=0: return False
            position.append((i,j))
    return True
def dfs(z,cnt,paper,paper_pos,paper_state):
    global result
    if cnt>=result: return
    if z==0:
        result=min(result,cnt)
        return
    for x,y in paper_pos:
        if paper[x][y]!=0: continue
        for dist in range(5,0,-1):
            if paper_state[dist]<=0: continue
            position=[]
            if square(x,y,dist,position):
                for nx,ny in position:
                    paper[nx][ny]=dist
                paper_state[dist]-=1
                dfs(z-len(position),cnt+1,paper,paper_pos,paper_state)
                for nx,ny in position:
                    paper[nx][ny]=0
                paper_state[dist]+=1
        break
dfs(len(paper_pos),0,paper,paper_pos,paper_state)
if result==25:
    result=-1
print(result)