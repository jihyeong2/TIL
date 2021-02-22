def isPossible(x,y,num):
    if num in maps[x]:
        return False
    for i in range(9):
        if maps[i][y]==num:
            return False
    a,b=x//3*3, y//3*3
    for i in range(3):
        for j in range(3):
            if maps[a+i][b+j]==num:
                return False
    return True

def sdoku(z,lim):
    global flag
    if z==lim:
        for row in maps:
            for col in row:
                print(col, end=' ')
            print()
        flag=True

    else:
        x,y=blank[z]
        for i in range(1,10):
            if isPossible(x,y,i):
                maps[x][y]=i
                sdoku(z+1,lim)
                if flag: return
                maps[x][y]=0

maps=[list(map(int, input().split())) for _ in range(9)]
blank=[(i,j) for i in range(9) for j in range(9) if maps[i][j]==0 ]
print(blank)
flag=False
sdoku(0,len(blank))