T=int(input())
for tc in range(1,T+1):
    n=int(input())
    num=list(map(int,input().split()))
    num.sort()
    result=''
    for i in range(5):
        result+=str(num[n-1-i])+' '
        result+=str(num[i])+' '
    print('#{} {}'.format(tc,result))