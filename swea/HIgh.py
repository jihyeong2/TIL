import sys
from itertools import combinations
sys.stdin=open("input.txt","r")
T=int(input())
for tc in range(1,T+1):
    n,b=map(int,input().split())
    h=list(map(int, input().split()))
    result,max_sum=9999999,sum(h)
    for i in range(1,n+1):
        tmp=combinations(h,i)
        for row in tmp:
            sum=0
            for x in row:
                sum+=x
            if b<=sum<result:
                result=sum
    print('#{} {}'.format(tc,result-b))