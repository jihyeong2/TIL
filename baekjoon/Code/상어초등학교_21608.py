n=int(input())
order,likes=[],[0]*((n**2)+1)
for _ in range(n**2):
    temp=list(map(int, input().split()))
    order.append(temp[0])
    likes[temp[0]]=temp[1:]
maps=[[0]*n for _ in range(n)]
dx,dy=(-1,1,0,0),(0,0,-1,1)
for student in order:
    max_friends, max_blank = -1, -1
    maxX, maxY = -1, -1
    for i in range(n):
        for j in range(n):
            if maps[i][j]!=0: continue
            friends_cnt,blank_cnt=0,0
            for dir in range(4):
                nx,ny=i+dx[dir],j+dy[dir]
                if 0<=nx<n and 0<=ny<n:
                    if maps[nx][ny]==0:
                        blank_cnt+=1
                    else:
                        if maps[nx][ny] in likes[student]:
                            friends_cnt+=1

            if friends_cnt>max_friends:
                max_friends=friends_cnt
                max_blank=blank_cnt
                maxX,maxY=i,j
            elif friends_cnt==max_friends:
                if blank_cnt>max_blank:
                    max_blank=blank_cnt
                    maxX,maxY=i,j
    maps[maxX][maxY]=student

res=0
for i in range(n):
    for j in range(n):
        if maps[i][j]==0: continue
        num=maps[i][j]
        cnt=0
        for dir in range(4):
            nx, ny = i + dx[dir], j + dy[dir]
            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] in likes[num]:
                cnt+=1
        if cnt>0:
            res+=10**(cnt-1)
print(res)