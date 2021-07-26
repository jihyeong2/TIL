from collections import deque
def solution(n, m, image):
    def BFS(a, b, val, image, visit):
        q = deque()
        q.append((a,b))
        visit[a][b] = 1
        dx,dy = (-1,1,0,0),(0,0,-1,1)
        while q:
            x,y = q.popleft()
            for d in range(4):
                nx,ny = x+dx[d], y+dy[d]
                if 0<=nx<n and 0<=ny<m and image[nx][ny] == val and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
    answer = 0
    visit = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visit[i][j]: continue
            BFS(i,j,image[i][j],image,visit)
            answer+=1
    return answer

solution(2,3,[[1, 2, 3], [3, 2, 1]])
solution(3,2,[[1, 2], [1, 2], [4, 5]])