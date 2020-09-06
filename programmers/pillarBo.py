def isPossible(x,y,target,maps):
    if target==2: # 기둥
        if x==n or maps[x][y]%2==0 or maps[x][y]%3==0:
            return True
        else: return False
    else: # 보
        if (maps[x][y]%2==0 or maps[x][y+1]%2==0) or (maps[x][y]%9==0 and maps[x][y+1]%9==0):
            return True
        else: return False
def install(x,y,a,maps,n,answer):
    target = a + 2
    if target == 2:
        maps[x][y] *= target
        maps[x - 1][y] *= target
    else:
        maps[x][y] *= target
        maps[x][y + 1] *= target
    if isPossible(x,y,target,maps):
        if target==2:
            maps[x][y]//=target
            maps[x-1][y]//=target
        else:
            maps[x][y]//=target
            maps[x][y+1]//=target
    else: answer.append([y,n-x,a])
def delete(x,y,a,maps,n,answer):
    target = a + 2
    if target == 2:
        maps[x][y] //= target
        maps[x - 1][y] //= target
    else:
        maps[x][y] //= target
        maps[x][y + 1] //= target
    if
def solution(n, build_frame):
    answer = []
    maps=[[1]*(n+1) for _ in range(n+1)]
    for y,x,a,b in build_frame:
        if b==0:
            delete(n-x,y,a,maps,n,answer)
        else:
            install(n-x,y,a,maps,n,answer)
    answer.sort(key=lambda x:(x[0],x[1],x[2]))
    for i in range(n+1):
        for j in range(n+1):
            print(maps[i][j],end=' ')
        print()
    print()
    return answer

n=5
f1=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
f2=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n,f1))
print(solution(n,f2))