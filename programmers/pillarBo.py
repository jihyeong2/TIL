def check(pb,x,y,n):
    if pb[y][x][0]==1:
        if not(y==0 or (x>0 and pb[y][x-1][1]==1) or pb[y][x][1]==1 or (y>0 and pb[y-1][x][0]==1)):
            return False
    if pb[y][x][1]==1:
        if not((y>0 and pb[y-1][x][0]==1) or (y>0 and x<n and pb[y-1][x+1][0]==1) or (0<x<n and pb[y][x-1][1]==1 and pb[y][x+1][1]==1)):
            return False
    return True
def solution(n, build_frame):
    answer = []
    pb=[]
    for i in range(n+1):
        pb.append([])
        for j in range(n+1):
            pb[i].append([0,0])
    for frame in build_frame:
        x,y,a,b=frame
        if b==1:
            pb[y][x][a]+=1
            if not check(pb,x,y,n):
                pb[y][x][a]-=1
        else:
            pb[y][x][a] -= 1
            if a==0: #기둥
                if not (check(pb,x,y,n) and check(pb,x-1,y+1,n) and check(pb,x,y+1,n)):
                    pb[y][x][a]+=1
            else: #보
                if not (check(pb,x,y,n) and check(pb,x-1,y,n) and check(pb,x+1,y,n)):
                    pb[y][x][a]+=1
    for i in range(n+1):
        for j in range(n+1):
            if pb[i][j][0]==1: answer.append([j,i,0])
            if pb[i][j][1]==1: answer.append([j,i,1])
    answer.sort(key=lambda x : (x[0],x[1],x[2]))
    return answer
n=5
f1=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
f2=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n,f1))
print(solution(n,f2))
