def perm(z,opers):
    if z==n-1:
        global max_r,min_r
        val=numbers[0]
        for i,oper in enumerate(opers):
            if oper==0:
                val+=numbers[i+1]
            elif oper==1:
                val-=numbers[i+1]
            elif oper==2:
                val*=numbers[i+1]
            else:
                val=-(abs(val)//numbers[i+1]) if val<0 else val//numbers[i+1]
        max_r=max(max_r,val)
        min_r=min(min_r,val)
    else:
        for i in range(4):
            if op[i]==0: continue
            op[i]-=1
            perm(z+1,opers+[i])
            op[i]+=1
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    op=list(map(int, input().split()))
    max_r,min_r=float('-inf'),float('inf')
    numbers=list(map(int, input().split()))
    perm(0,[])
    print('#{} {}'.format(tc,max_r-min_r))