def solution(progresses, speeds):
    answer = []
    idx = 0
    while idx < len(progresses):
        for i in range(idx, len(progresses)):
            if progresses[i] >= 100: continue
            progresses[i] += speeds[i]
        cnt = 0
        for i in range(idx, len(progresses)):
            if progresses[i] >= 100 :
                cnt += 1
            else : break
        if cnt > 0:
            idx += cnt
            answer.append(cnt)
    print(answer)
    return answer

solution([93,30,55],[1,30,5])