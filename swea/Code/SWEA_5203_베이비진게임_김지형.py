def isRun(cnt):
    res=0
    for i in range(10):
        if cnt[i]: res+=1
        else: res=0
        if res>=3: return True
    return False
def isTriplet(cnt):
    for i in range(10):
        if cnt[i]>=3: return True
    return False
T=int(input())
for tc in range(1,T+1):
    arr=list(map(int,input().split()))
    a_cnt,b_cnt,result=[0]*10,[0]*10,0
    for i in range(len(arr)):
        if i%2==0:
            a_cnt[arr[i]]+=1
        else:
            b_cnt[arr[i]]+=1
        if isRun(a_cnt) or isTriplet(a_cnt):
            result=1
            break
        if isRun(b_cnt) or isTriplet(b_cnt):
            result=2
            break
    print('#{} {}'.format(tc,result))