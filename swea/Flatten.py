import sys
sys.stdin=open("input.txt","r")
for tc in range(1,11):
    n=int(input())
    box=list(map(int,input().split()))
    while True:
        if n==0 or max(box)-min(box)<=1:
            break
        max_height=max(box)
        min_height = min(box)
        box[box.index(max_height)]-=1
        box[box.index(min_height)]+=1
        n-=1
    print(f'#{tc} {max(box)-min(box)}')