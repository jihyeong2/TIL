import sys
sys.stdin=open("input.txt","r")
for tc in range(1,11):
    n=int(input())
    maps,reds,blues,tmpR,tmpB=[],[],[],[],[]
    for i in range(n):
        temp=list(map(int, input().split()))
        for j in range(n):
            if temp[j]==0: continue
            elif temp[j]==1: reds.append([i,j])
            elif temp[j]==2: blues.append([i,j])
        maps.append(temp)
    result=0
    while True:
        if len(reds)==0 and len(blues)==0: break
        for x,y in blues:
            nx,ny=x-1,y
            if nx<0 or ny<0 or nx>=n or ny>=n:
                maps[x][y]=0
                continue
            if maps[nx][ny]==2: continue
            elif maps[nx][ny]==1:   result+=1
            else:
                maps[x][y],maps[nx][ny]=0,2
                tmpB.append([nx,ny])
        for x,y in reds:
            nx,ny=x+1,y
            if nx<0 or ny<0 or nx>=n or ny>=n:
                maps[x][y]=0
                continue
            if maps[nx][ny]==1: continue
            elif maps[nx][ny]==2:   result+=1
            else:
                maps[x][y],maps[nx][ny]=0,1
                tmpR.append([nx,ny])
        blues.clear()
        reds.clear()
        for x,y in tmpB:
            blues.append([x,y])
        for x,y in tmpR:
            reds.append([x,y])
        tmpB.clear()
        tmpR.clear()
    print('#{} {}'.format(tc,result//2))