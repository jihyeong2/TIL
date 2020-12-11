dr,dc=(-1,-1,0,1,1,1,0,-1),(0,1,1,1,0,-1,-1,-1)

n,m,k=map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
ball=[]
for i in range(m):
    r,c,m,s,d=map(int, input().split())
    ball.append([r-1,c-1,m,s,d])

for _ in range(k):
    for i in range(len(ball)):
        r,c,m,s,d=ball[i]
        nr,nc=(r+dr[d]*s)%n,(c+dc[d]*s)%n
        ball[i][0],ball[i][1]=nr,nc
        board[nr][nc].append(i)

    n_ball=[]
    for i in range(n):
        for j in range(n):
            if len(board[i][j])==0: continue
            elif len(board[i][j])==1:
                n_ball.append(ball[board[i][j][0]])
            else:
                sum_m,sum_s,odd,even,cnt=0,0,0,0,0
                for num in board[i][j]:
                    r, c, m, s, d = ball[num]
                    sum_m,sum_s=sum_m+m,sum_s+s
                    cnt+=1
                    if d%2==0: even+=1
                    else: odd+=1
                avg_m=sum_m//5
                avg_s=sum_s//cnt
                if avg_m >0:
                    start=1
                    if (even!=0 and odd==0) or (even==0 and odd!=0):
                        start=0
                    for dir in range(start,8,2):
                        n_ball.append([i,j,avg_m,avg_s,dir])
            board[i][j].clear()
    ball.clear()
    for r,c,m,s,d in n_ball:
        ball.append([r,c,m,s,d])

result=0
for i in range(len(ball)):
    result+=ball[i][2]

print(result)