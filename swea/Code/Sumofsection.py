T=int(input())
for tc in range(1,T+1):
    n,m=map(int, input().split())
    num=list(map(int, input().split()))
    S=[0]*n
    S[0]=num[0]
    for i in range(1,n):
        S[i]=S[i-1]+num[i]
    max_result=S[m-1]
    min_result=S[m-1]
    for i in range(m,n):
        temp=S[i]-S[i-m]
        max_result=max(max_result,temp)
        min_result=min(min_result,temp)
    print(f'#{tc} {max_result-min_result}')