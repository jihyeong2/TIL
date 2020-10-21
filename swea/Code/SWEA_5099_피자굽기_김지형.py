import sys
sys.stdin=open("input.txt","r")
def bake(n,m,pizzas):
    q,next,pizza=[i for i in range(n)],n,0
    while q:
        size=len(q)
        while size:
            pizza=q.pop(0)
            pizzas[pizza]//=2
            if pizzas[pizza]==0:
                if next<m:
                    q.append(next)
                    next+=1
            else:
                q.append(pizza)
            size-=1
    return pizza+1
T=int(input())
for tc in range(1,T+1):
    n,m=map(int, input().split())
    pizzas=list(map(int, input().split()))
    result=bake(n,m,pizzas)
    print('#{} {}'.format(tc,result))