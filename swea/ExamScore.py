import sys
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    scores=list(map(int, input().split()))
    visit=[0]*(sum(scores)+1)
    visit[0],result=1,[0]
    for score in scores:
        size=len(result)
        for idx in range(size):
            if visit[result[idx]+score]: continue
            result.append(result[idx]+score)
            visit[result[idx]+score]=1
    print('#{} {}'.format(tc,len(result)))