# def perm(z,max_r):
#     global result
#     if max_r<=result : return
#     if z==n:
#         result=max(max_r,result)
#     else:
#         for i in range(n):
#             if visit[i]: continue
#             visit[i]=1
#             perm(z+1,max_r*p[z][i]*0.01)
#             visit[i]=0
# T=int(input())
# for tc in range(1,T+1):
#     n=int(input())
#     p=[list(map(int, input().split())) for _ in range(n)]
#     visit,result=[0]*n,0
#     perm(0,100)
#     print('#{} {}'.format(tc,'%0.6f'%result))
def quickSort(arr):
    if len(arr)<=1:
        return arr
    p,l,r=arr[0],[],[]
    for i in range(1,len(arr)):
        if arr[i]<=p : l.append(arr[i])
        else : r.append(arr[i])
    return quickSort(l) + [p] + quickSort(r)
print(quickSort([11,1,3,13,5,17]))

def powerSet(arr):
    for i in range(2**len(arr)):
        tmp=[]
        for j in range(len(arr)):
            if i & 1<<j: tmp.append(arr[j])
        if tmp and sum(tmp)==10:
            print(tmp)
powerSet([1,2,3,4,5,6,7,8,9,10])

def preOrder(idx):
    print(idx,end=' ')
    for n_i in v[idx]:
        preOrder(n_i)
def inOrder(idx):
    if len(v[idx])>=1: inOrder(v[idx][0])
    print(idx, end=' ')
    if len(v[idx])>=2: inOrder(v[idx][1])
def postOrder(idx):
    for n_i in v[idx]:
        postOrder(n_i)
    print(idx,end=' ')
edge=[1,2,1,3,2,4,3,5,3,6,4,7,5,8,5,9,6,10,6,11,7,12,11,13]
v=[[] for _ in range(14)]
for i in range(0,len(edge),2):
    v[edge[i]].append(edge[i+1])
preOrder(1)
print()
inOrder(1)
print()
postOrder(1)