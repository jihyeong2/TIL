import sys
sys.stdin=open("input.txt","r")
def goDown(x,y,length,lad,visit):
    visit.add((x,y))
    if x>=99:
        return length
    else:
        if 0<=y-1<100 and lad[x][y-1]==1 and (x,y-1) not in visit:
            return goDown(x,y-1,length+1,lad,visit)
        if 0<=y+1<100 and lad[x][y+1]==1 and (x,y+1) not in visit:
            return goDown(x,y+1,length+1,lad,visit)
        return goDown(x+1,y,length+1,lad,visit)
for _ in range(10):
    tc=int(input())
    lad=[list(map(int,input().split())) for _ in range(100)]
    max_l,result=999999999,-1
    for j in range(100):
        if lad[0][j]==0: continue
        visit=set()
        visit.add((0,j))
        temp_l=goDown(0,j,0,lad,visit)
        if max_l>temp_l:
            max_l,result=temp_l,j
    print('#{} {}'.format(tc,result))