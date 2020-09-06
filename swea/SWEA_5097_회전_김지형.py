import sys
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    n,m=map(int, input().split())
    q=list(map(int, input().split()))
    for _ in range(m):
        first=q.pop(0)
        q.append(first)
    print('#{} {}'.format(tc,q[0]))