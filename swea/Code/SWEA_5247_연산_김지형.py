def bfs():
    q=[(n,0)]
    nums=[0]*1000001
    nums[n]=1
    cnt=1
    while q:
        x,depth=q.pop(0)
        print(x,depth)
        cnt+=1
        if x+1==m or x-1==m or x*2==m or x-10==m:
            print(cnt)
            return depth+1
        if x-1>0 and not nums[x-1]:
            nums[x - 1] = 1
            q.append((x-1,depth+1))
        if x-10>0 and not nums[x-10]:
            nums[x-10]=1
            q.append((x-10,depth+1))
        if x+1<=1000000 and not nums[x+1]:
            nums[x + 1] = 1
            q.append((x+1,depth+1))
        if x*2<=1000000 and not nums[x*2]:
            nums[x*2]=1
            q.append((x*2,depth+1))

T=int(input())
for tc in range(1,T+1):
    n,m=map(int, input().split())
    result=bfs()
    print('#{} {}'.format(tc,result))