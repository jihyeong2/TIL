# import sys
# sys.stdin=open("input.txt","r")
def count_brick(bricks):
    pass
def falling_brick(bricks):
    pass
def break_brick(z,bricks):
    pass
T=int(input())
result=987654321
for tc in range(1,T+1):
    n,w,h = map(int, input().split())
    bricks=list()
    result=987654321
    for _ in range(h):
        bricks.append(list(map(int, input().split())))
    print(bricks)
    