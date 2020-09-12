from itertools import permutations
def solution(n, weak, dist):
    answer = len(dist)+1
    length=len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    for i in range(length):
        new_weak=weak[i:i+length]
        friends_perm=permutations(dist,len(dist))
        for friends in friends_perm:
            distance=new_weak[0]+friends[0]
            f_cnt,f_idx=1,0
            for j in range(length):
                if new_weak[j]>distance:
                    f_cnt,f_idx=f_cnt+1,f_idx+1
                    if f_cnt>len(friends):
                        break
                    distance=new_weak[j]+friends[f_idx]
            answer=min(answer,f_cnt)
    if answer==len(dist)+1:
        return -1
    return answer
weak=[1,5,6,10]
dist=[1,2,3,4]
print(solution(12,weak,dist))
print(solution(12,[1, 3, 4, 9, 10],[3,5,7]))