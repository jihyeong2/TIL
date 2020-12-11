def solution(board, moves):
    def find(col):
        for i in range(n):
            if board[i][col]!=0:
                return i
        return -1
    answer = 0
    n=len(board)
    print(n)
    s=[]
    for col in moves:
        col-=1
        row=find(col)
        if row==-1: continue
        if len(s)==0:
            s.append(board[row][col])
        else:
            if s[-1]==board[row][col]:
                answer+=1
                s.pop(-1)
            else:
                s.append(board[row][col])
        board[row][col] = 0
    return answer*2

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))