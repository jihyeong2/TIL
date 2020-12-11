def solution(progresses, speeds):
    answer = []
    t=0
    while progresses:
        t+=1
        for i in range(len(progresses)):
            progresses[i]=progresses[i]+speeds[i] if progresses[i]+speeds[i]<100 else 100
        cnt=0
        while progresses and progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1
        if cnt!=0: answer.append(cnt)
    return answer

print(solution([93,30,55],[1,30,5]))