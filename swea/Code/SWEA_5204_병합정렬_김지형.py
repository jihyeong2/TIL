def merge(arr,l1,r1,l2,r2):
    s1,s2,tmp=l1,l2,[]
    global result
    if arr[r1]>arr[r2]: result+=1
    while s1<r1 and s2<r2:
        if arr[s1]<arr[s2]:
            tmp.append(arr[s1])
            s1+=1
        else:
            tmp.append(arr[s2])
            s2+=1
    while s1<r1:
        tmp.append(arr[s1])
        s1+=1
    while s2<r2:
        tmp.append(arr[s2])
        s2+=1
    for i in range(len(tmp)):
        arr[i+l1]=tmp[i]
def mergeSort(arr,l,r):
    if l>=r: return
    mid=(l+r)//2
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,mid+1,r)
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=list(map(int,input().split()))
    result=0
    mergeSort(arr,0,n-1)
    print(arr)
    print('#{} {} {}'.format(tc,arr[n//2],result))