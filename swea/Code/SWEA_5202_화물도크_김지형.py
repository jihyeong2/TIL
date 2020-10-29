import sys
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    times=[]
    for _ in range(n):
        s,e=map(int,input().split())
        times.append([s,e])
    times.sort(key=lambda x : x[1])
    result = 1
    s,e=times[0]
    for i in range(1,n):
        n_s,n_e=times[i]
        if n_s<e: continue
        result+=1
        s,e=n_s,n_e
    print('#{} {}'.format(tc,result))