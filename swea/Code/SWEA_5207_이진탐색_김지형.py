# import sys
# sys.stdin=open("input.txt","r")
# def Bsearch(l,r,num):
#     flag=0
#     while l<=r:
#         mid=(l+r)//2
#         if A[mid]<num :
#             l=mid+1
#             if flag == 1: return 0
#             flag=1
#         elif A[mid]>num :
#             r=mid-1
#             if flag==-1: return 0
#             flag=-1
#         else : return 1
#     return 0
# T=int(input())
# for tc in range(1,T+1):
#     n,m=map(int, input().split())
#     A=list(map(int, input().split()))
#     B=list(map(int, input().split()))
#     A.sort()
#     result=0
#     for num in B:
#         result+=Bsearch(0,n-1,num)
#     print('#{} {}'.format(tc,result))
def Bsearch(s,e,val):
    flag=0
    while s<=e:
        mid=(s+e)//2
        if A[mid]>val:
            e=mid-1
            if flag==1:  return 0
            flag=1
        elif A[mid]<val:
            s=mid+1
            if flag==-1: return 0
            flag=-1
        else : return 1
    return 0
T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    A=sorted(list(map(int,input().split())))
    B=list(map(int,input().split()))
    result=0
    for num in B:
        result+=Bsearch(0,n-1,num)
    print('#{} {}'.format(tc,result))