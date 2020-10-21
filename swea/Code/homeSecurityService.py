import sys
sys.stdin=open("input.txt","r")
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def dist(x,y,xx,yy):
    return abs(x-xx)+abs(y-yy)
def service(a,b,leng,maps):
    res=0
    for x,y in house:
        if dist(x,y,a,b)<leng: res+=1
    if res*m>=money : return res
    return 0
T=int(input())
for tc in range(1,T+1):
    n,m=map(int, input().split())
    maps=[list(map(int, input().split())) for _ in range(n)]
    house = list()
    for i in range(n):
        for j in range(n):
            if maps[i][j]==1:
                house.append([i,j])
    hCnt=len(house)
    result=-1
    for i in range(n):
        for j in range(n):
            k=1
            while True:
                money = (k * k) + (k - 1) * (k - 1)
                if hCnt * m < money: break
                result=max(result,service(i,j,k,maps))
                k+=1
    print('#{} {}'.format(tc,result))