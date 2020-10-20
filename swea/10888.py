from itertools import combinations
def calPlace(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    maps=[list(map(int, input().split())) for _ in range(n)]
    houses,stores=[],[]
    result=float('inf')
    for i in range(n):
        for j in range(n):
            if maps[i][j]==1:
                houses.append((i,j))
            elif maps[i][j]>1:
                stores.append((i,j))
    for i in range(1,len(stores)+1):
        stores_comb=list(map(list,combinations(stores,i)))
        for combs in stores_comb:
            dists = [40] * len(houses)
            money = 0
            for x,y in combs:
                for idx,info in enumerate(houses):
                    dists[idx]=min(dists[idx],calPlace(x,y,info[0],info[1]))
                money+=maps[x][y]
            money+=sum(dists)
            result=min(result,money)
    print('#{} {}'.format(tc,result))