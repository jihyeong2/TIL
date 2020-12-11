def solution(priorities, location):

    def isPossible(num):
        for idx,num2 in priorities:
            if num2>num: return False
        return True

    for i in range(len(priorities)):
        priorities[i]=(i,priorities[i])
    answer = 0
    while True:
        idx,num=priorities.pop(0)
        if isPossible(num):
            answer+=1
            if idx==location:
                return answer
        else:
            priorities.append((idx,num))
    return answer

print(solution([1,1,9,1,1,1],0))