def merge(left,right):
    s1,s2,e1,e2,tmp=0,0,len(left),len(right),[]
    global result
    if left[-1]>right[-1] : result+=1
    while s1<e1 and s2<e2:
        if left[s1]<=right[s2]:
            tmp.append(left[s1])
            s1+=1
        else:
            tmp.append(right[s2])
            s2+=1
    while s1<e1:
        tmp.append(left[s1])
        s1+=1
    while s2<e2:
        tmp.append(right[s2])
        s2+=1
    return tmp
def mergeSort(arr):
    if len(arr)<=1: return arr
    left,right=arr[:len(arr)//2],arr[len(arr)//2:]
    left=mergeSort(left)
    right=mergeSort(right)
    sorted_arr=merge(left,right)
    return sorted_arr
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=list(map(int,input().split()))
    result=0
    sorted_arr=mergeSort(arr)
    print('#{} {} {}'.format(tc,sorted_arr[n//2],result))