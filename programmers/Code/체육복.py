def solution(n, lost, reserve):
    students = [1] * (n+1)
    for i in lost:
        students[i]-=1
    for i in reserve:
        students[i]+=1
    for i in lost:
        if i>0: continue
        if i-1>0 and students[i-1]>1:
            students[i-1]-=1
            students[i]+=1
            continue
        if i+1<=n and students[i+1]>1:
            students[i+1]-=1
            students[i]+=1
    answer = 0
    for i in range(1,n+1):
        if students[i]>0:
            answer+=1
    return answer

solution(5,[2, 4],[1, 3, 5])
solution(5,[2, 4],[3])
solution(3,[3],[1])