import sys
sys.stdin=open("input.txt","r")
T=int(input())
def checkArrow(x):
    if x>=8: return x%8
    elif x<0: return x+8
    else: return x
def left(num,dir):
    if num<0: return
    before=checkArrow(arrow[num+1]-2)
    current=checkArrow(arrow[num]+2)
    if magnetic[num][current]==magnetic[num+1][before]: return
    left(num-1,-dir)
    arrow[num]=checkArrow(arrow[num]-dir)
def right(num,dir):
    if num>=4: return
    before=checkArrow(arrow[num-1]+2)
    current=checkArrow(arrow[num]-2)
    if magnetic[num][current]==magnetic[num-1][before]: return
    right(num+1,-dir)
    arrow[num]=checkArrow(arrow[num]-dir)
for tc in range(1,T+1):
    k=int(input())
    magnetic=[list(map(int, input().split())) for _ in range(4)]
    arrow=[0]*4
    for times in range(k):
        first_num,first_dir=map(int,input().split())
        first_num-=1
        left(first_num-1,-first_dir)
        right(first_num+1,-first_dir)
        arrow[first_num]=checkArrow(arrow[first_num]-first_dir)
    result=0
    for i in range(4):
        if magnetic[i][arrow[i]]==1:
            result+=2**i
    print('#{} {}'.format(tc,result))