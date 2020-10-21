from itertools import combinations
import sys
sys.stdin=open("input.txt","r")
def test(arr):
    for j in range(W):
        before,cnt=arr[0][j],1
        for i in range(1,D):
            if before==arr[i][j]:
                cnt+=1
            else:
                before,cnt=arr[i][j],1
            if cnt>=K: break
        else:
            return False
    return True
T=int(input())
for tc in range(1,T+1):
    D,W,K=map(int,input().split())
    films=[list(map(int,input().split())) for _ in range(D)]
    if K==1 or test(films):
        result=0
    else:
        flag=0
        for i in range(1,K):
            combs=combinations(range(D),i)
            for comb in combs:
                copy=[row[:] for row in films]
                for comb_i in comb:
                    copy[comb_i]=[0]*W
                    if test(copy):
                        flag,result=1,i
                        break
                for comb_i in comb:
                    copy[comb_i]=[1]*W
                    if test(copy):
                        flag,result=1,i
                        break
                if flag: break
            if flag: break
        else:
            result=K
    print('#{} {}'.format(tc,result))