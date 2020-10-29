import sys
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    n,m=map(int, input().split())
    container=list(map(int, input().split()))
    truck=list(map(int, input().split()))
    # truck.sort(key=lambda x : -x)
    result=0
    visit=[0]*n
    for i in range(m):
        val,idx=0,0
        for j in range(n):
            if visit[j]: continue
            if truck[i]>=container[j]:
                idx=idx if val>container[j] else j
                val=container[idx]
        if val==0: continue
        result+=val
        visit[idx]=1
    print('#{} {}'.format(tc,result))
