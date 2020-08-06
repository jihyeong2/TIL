import sys
sys.stdin=open("input.txt","r")
def comb(z,idx,n,k,set,subset):
    result=0
    if z>=n:
        if sum(subset)!=k:return 0
        return 1
    else :
        for i in range(idx,12):
            if set[i] in subset:continue
            subset.append(set[i])
            result+=comb(z+1,i,n,k,set,subset)
            subset.pop()
    return result
T=int(input())
for tc in range(1,T+1):
    n,k=map(int, input().split())
    set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    subset=[]
    result=comb(0,0,n,k,set,subset)
    print(f'#{tc} {result}')
