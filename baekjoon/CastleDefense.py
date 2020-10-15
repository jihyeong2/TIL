from itertools import permutations,combinations
import copy
def cal_dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)
n,m,d=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
result=float('-inf')
monsterCnt=0
for row in arr:
    monsterCnt+=row.count(1)
combs = list(combinations(range(m), 3))
for comb in combs:
    hunter = []
    monster=monsterCnt
    killMonsterCnt=0
    maps=copy.deepcopy(arr)
    for y in comb:
        hunter.append((n,y))
    while monster:
        target=[]
        for x, y in hunter:
            t_x,t_y,t_dist=-1,-1,11
            for i in range(n-1,n-1-d,-1):
                if i<0 : break
                for j in range(m):
                    dist=cal_dist(x,y,i,j)
                    if maps[i][j]==1 and dist<=d :
                        if dist<t_dist:
                            t_x,t_y,t_dist=i,j,dist
                        elif dist==t_dist:
                            if j<t_y:
                                t_x,t_y=i,j
                if t_x!=-1: break
            if t_x!=-1 and (t_x,t_y) not in target:
                target.append((t_x,t_y))
        for x,y in target:
            maps[x][y]=0
        killMonsterCnt+=len(target)
        monster-=len(target)
        monster-=maps[n-1].count(1)
        maps[n-1]=[0]*m
        for i in range(n-1,0,-1):
            maps[i],maps[i-1]=maps[i-1],maps[i]
        # print('남은 적 : {} / 잡은 적 : {}'.format(monster,killMonsterCnt))
        # for i in range(n):
        #     for j in range(m):
        #         print(maps[i][j],end=' ')
        #     print()
        # print()
    result=max(result,killMonsterCnt)
print(result)