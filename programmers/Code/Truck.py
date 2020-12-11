def solution(bridge_length, weight, truck_weights):
    q=[]
    t,idx,num,sum=0,0,len(truck_weights),0
    while num:
        t+=1
        for i in range(len(q)):
            w,d=q.pop(0)
            if d+1>bridge_length:
                sum-=w
                num-=1
                continue
            q.append((w,d+1))
        if idx<len(truck_weights) and sum+truck_weights[idx]<=weight:
            q.append((truck_weights[idx],1))
            sum+=truck_weights[idx]
            idx+=1
    return t

print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))