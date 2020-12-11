n,k=map(int, input().split())
belt=list(map(int, input().split()))
robot=[0]*n
result=0
while True:
    result+=1
    b_belt,b_robot=belt[0],robot[0]
    for i in range(1,2*n):
        if i<n:
            robot[i],b_robot=b_robot,robot[i]
        belt[i],b_belt=b_belt,belt[i]
    belt[0],robot[0]=b_belt,0
    if robot[n-1]==1:
        robot[n-1]=0
    for i in range(n-2,0,-1):
        if robot[i]==1 and robot[i+1]==0 and belt[i+1]>0:
            robot[i+1],robot[i]=1,0
            belt[i+1]-=1
            if belt[i+1]<=0: k-=1
    if belt[0]>0:
        robot[0]=1
        belt[0]-=1
        if belt[0]==0: k-=1
    if k<=0: break
print(result)