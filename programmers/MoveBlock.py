def solution(board):
    n=len(board)
    dx,dy=(-1,1,0,0),(0,0,-1,1)
    row_rotate_x1,row_rotate_y1=(-1,0,-1,0),(1,1,0,0)
    row_rotate_x2,row_rotate_y2=(0,1,0,1),(0,0,-1,-1)
    row_check_x,row_check_y=(-1,1,-1,1),(0,0,1,1)
    col_rotate_x1,col_rotate_y1=(1,1,0,0),(-1,0,-1,0)
    col_rotate_x2,col_rotate_y2=(0,0,-1,-1),(0,1,0,1)
    col_check_x,col_check_y=(0,0,1,1),(-1,1,-1,1)
    q,visit=[],set()
    q.append((0,0,0,1,0,False))
    visit.add((0,0,0,1))
    while q:
        x1,y1,x2,y2,dist,state=q.pop(0)
        # print(x1, y1, x2, y2, dist, state)
        # 종료조건
        if x2 == n-1 and y2 ==  n-1 :
            answer=dist
            break
        # 로봇 상하좌우 이동
        for dir in range(4):
            nx1,ny1,nx2,ny2=x1+dx[dir],y1+dy[dir],x2+dx[dir],y2+dy[dir]
            # print(x1,y1,x2,y2)
            # print(nx1, ny1, nx2, ny2)
            # print()
            if nx1 < 0 or ny1 < 0 or nx1 >= n or ny1 >= n or board[nx1][ny1] == 1: continue
            if nx2 < 0 or ny2 < 0 or nx2 >= n or ny2 >= n or board[nx2][ny2] == 1: continue

            if (nx1,ny1,nx2,ny2) not in visit:
                visit.add((nx1,ny1,nx2,ny2))
                q.append((nx1,ny1,nx2,ny2,dist+1,state))
        # 로봇 회전
        for rotate_dir in range(4):
            if not state :
                # 가로
                check_x,check_y=x1+row_check_x[rotate_dir],y1+row_check_y[rotate_dir]
                nx1,ny1=x1+row_rotate_x1[rotate_dir], y1+row_rotate_y1[rotate_dir]
                nx2,ny2=x2+row_rotate_x2[rotate_dir], y2+row_rotate_y2[rotate_dir]
                # state=1
            else:
                # 세로
                check_x,check_y=x1+col_check_x[rotate_dir],y1+col_check_y[rotate_dir]
                nx1,ny1=x1+col_rotate_x1[rotate_dir], y1+col_rotate_y1[rotate_dir]
                nx2,ny2=x2+col_rotate_x2[rotate_dir], y2+col_rotate_y2[rotate_dir]
                # state=0
            if nx1 < 0 or ny1 < 0 or nx1 >= n or ny1 >= n or board[nx1][ny1] == 1: continue
            if nx2 < 0 or ny2 < 0 or nx2 >= n or ny2 >= n or board[nx2][ny2] == 1: continue
            if not board[check_x][check_y] and (nx1, ny1, nx2, ny2) not in visit:
                visit.add((nx1, ny1, nx2, ny2))
                q.append((nx1, ny1, nx2, ny2, dist + 1, not state))


    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))