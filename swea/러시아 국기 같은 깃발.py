import sys
sys.stdin=open("input.txt","r")
# dic={'0':'W','1':'B','2':'R'}
# def comb(z,idx,sum,n,m,maps):
#     global result
#     if sum>=result: return
#     if z==3:
#         if idx!=n: return
#         if result>sum:
#             result=sum
#             return
#     for length in range(1,n-1):
#         if idx+length>n: continue
#         cnt = 0
#         for i in range(idx,idx+length):
#             for j in range(m):
#                 if maps[i][j]!=dic[str(z)]:
#                     cnt+=1
#         comb(z+1,idx+length,sum+cnt,n,m,maps)

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    maps=[list(input()) for _ in range(n)]
    count_flag=[]
    for row in maps:
        count_flag.append([m-row.count('W'),m-row.count('B'),m-row.count('R')])
    result=987654321
    for w in range(1,n-1):
        for b in range(1,n-1):
            for r in range(1,n-1):
                if w+b+r!=n: continue
                sum=0
                for i in range(w): sum+=count_flag[i][0]
                for i in range(w,w+b): sum+=count_flag[i][1]
                for i in range(w+b,w+b+r): sum+=count_flag[i][2]
                result=min(result,sum)
    print('#{} {}'.format(tc,result))