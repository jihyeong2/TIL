def solution(x,y,d1,d2):
    global result

    check=[[0]*n for _ in range(n)]
    # 경계선 처리
    for d in range(d1+1):
        check[x+d][y-d]=5
        check[x + d2 + d][y + d2 - d] = 5
    for d in range(d2+1):
        check[x+d][y+d]=5
        check[x + d1+d][y - d1 + d] = 5

    # 1번
    for i in range(x+d1):
        for j in range(y+1):
            if check[i][j]==5: break
            check[i][j]=1
    # 2번
    for i in range(x+d2+1):
        for j in range(n-1,y,-1):
            if check[i][j] == 5: break
            check[i][j]=2
    # 3번
    for i in range(x+d1,n):
        for j in range(y-d1+d2):
            if check[i][j] == 5: break
            check[i][j]=3
    # 4번
    for i in range(x+d2+1,n):
        for j in range(n-1,y-d1+d2-1,-1):
            if check[i][j] == 5: break
            check[i][j]=4

    elect=[0]*6
    for i in range(n):
        for j in range(n):
            if check[i][j]==0:
                elect[5] += maps[i][j]
            else:
                elect[check[i][j]] += maps[i][j]
    elect.sort()
    result=min(result,elect[5]-elect[1])


n=int(input())
maps=[list(map(int, input().split())) for _ in range(n)]

result=40000
for i in range(n-2):
    for j in range(1,n-1):
        for d1 in range(1,n-1):
            for d2 in range(1,n-1):
                if i+d1+d2>=n or j-d1<0 or j+d2>=n: continue
                solution(i,j,d1,d2)

print(result)