def rotate(arr,m):
    rotated=[[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rotated[i][j]=arr[m-1-j][i]
    return rotated
def isKey(x,y,n,m,key,lock):
    new_lock=[[0]*(n + 2 * (m - 1)) for _ in range(n + 2 * (m - 1))]
    for i in range(m):
        for j in range(m):
            new_lock[x+i][y+j]=key[i][j]
    for i in range(m-1,n+m-1):
        for j in range(m-1,n+m-1):
            new_lock[i][j]+=lock[i-(m-1)][j-(m-1)]
            if new_lock[i][j]!=1: return False
    return True
def solution(key, lock):
    n,m=len(lock),len(key)
    for _ in range(4):
        for i in range(n+m-1):
            for j in range(n+m-1):
                if isKey(i,j,n,m,key,lock): return True
        key=rotate(key,m)
    return False
k=[[0,0,0],[1,0,0],[0,1,1]]
l=[[1,1,1],[1,1,0],[1,0,1]]
# solution(k,l)
print(solution(k,l))