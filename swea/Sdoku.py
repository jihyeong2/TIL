import sys
sys.stdin=open("input.txt","r")
T=int(input())
def isPossible(arr):
    for i in range(0,9,3):
        for j in range(0,9,3):
            count=[0 for _ in range(10)]
            for a in range(3):
                for b in range(3):
                    count[arr[i+a][i+b]]+=1
                    if count[arr[i+a][i+b]]>=2: return 0
    for i in range(9):
        count1=[0 for _ in range(10)]
        count2=[0 for _ in range(10)]
        for j in range(9):
            count1[arr[j][i]]+=1
            count2[arr[i][j]]+=1
            if count1[arr[j][i]]>=2: return 0
            if count2[arr[i][j]]>=2: return 0
    return 1
for tc in range(1,T+1):
    arr=[list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {isPossible(arr)}')