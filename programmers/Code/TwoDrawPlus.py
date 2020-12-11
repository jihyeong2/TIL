from itertools import combinations
def solution(numbers):
    answer = []
    n=len(numbers)
    com_numbers=list(combinations(numbers,2))
    for x,y in com_numbers:
        num=x+y
        if num not in answer:
            answer.append(num)
    answer.sort()
    return answer

print(solution([5,0,2,7]))