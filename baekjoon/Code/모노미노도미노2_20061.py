def make_block(type,t,x,y):
    if type : # blue
        if t==1:
            return [[x,0]]
        elif t==2:
            return [[x,-1],[x,0]]
        else:
            return [[x,0],[x+1,0]]
    else: # green
        if t==1:
            return [[0,y]]
        elif t==2:
            return [[0,y],[0,y+1]]
        else:
            return [[-1,y],[0,y]]

def blue_solution(t,x,y):
    global score

    # 블록 이동
    block=make_block(1,t,x,y)
    flag=False
    for i in range(1,6):
        n_block=[[b_x,b_y+1] for b_x,b_y in block]
        for n_x,n_y in n_block:
            if blue[n_x][n_y]:
                flag=True
        if flag:
            break
        block=n_block
    for b_x,b_y in block:
        blue[b_x][b_y]=1

    # 점수 획득 판단

    col=5
    while col>0:
        cnt=0
        for row in range(4):
            if blue[row][col]: cnt+=1
        if cnt<4:
            col-=1
        else:
            score+=1
            for j in range(col,0,-1):
                for i in range(4):
                    blue[i][j]=blue[i][j-1]
                    blue[i][j-1]=0

    # 연한 칸 처리

    c_cnt=0
    for j in range(2):
        for i in range(4):
            if blue[i][j]:
                c_cnt+=1
                break

    for _ in range(c_cnt):
        for j in range(5,0,-1):
            for i in range(4):
                blue[i][j]=blue[i][j-1]
                blue[i][j-1]=0


def green_solution(t,x,y):
    global score

    # 블록 이동
    block = make_block(0, t, x, y)
    flag = False
    for i in range(1,6):
        n_block = [[g_x+1, g_y] for g_x, g_y in block]
        for n_x, n_y in n_block:
            if green[n_x][n_y]:
                flag = True
        if flag:
            break
        block = n_block
    for g_x, g_y in block:
        green[g_x][g_y] = 1

    # 점수 획득 판단

    row = 5
    while row > 0:
        cnt = 0
        for col in range(4):
            if green[row][col]: cnt += 1
        if cnt < 4:
            row -= 1
        else:
            score += 1
            for i in range(row, 0, -1):
                for j in range(4):
                    green[i][j] = green[i-1][j]
                    green[i-1][j] = 0

    # 연한 칸 처리

    r_cnt = 0
    for i in range(2):
        for j in range(4):
            if green[i][j]:
                r_cnt += 1
                break

    for _ in range(r_cnt):
        for i in range(5, 0, -1):
            for j in range(4):
                green[i][j] = green[i-1][j]
                green[i-1][j] = 0


n=int(input())
blue=[[0]*6 for _ in range(4)]
green=[[0]*4 for _ in range(6)]
score=0
for _ in range(n):
    t,x,y = map(int, input().split())
    blue_solution(t,x,y)
    green_solution(t,x,y)
    print('그린')
    for row in green:
        print(row)
    print()
    print('블루')
    for row in blue:
        print(row)

green_cnt, blue_cnt=0,0
for i in range(4):
    for j in range(6):
        if blue[i][j]:
            blue_cnt+=1
for i in range(6):
    for j in range(4):
        if green[i][j]:
            green_cnt+=1

print(score)
print(green_cnt+blue_cnt)