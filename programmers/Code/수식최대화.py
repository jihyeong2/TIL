from itertools import permutations
from copy import deepcopy
def solution(expression):
    answer = 0
    numbers,opers=[],[]
    idx=0
    for i in range(len(expression)):
        if not '0'<=expression[i]<='9':
            numbers.append(int(expression[idx:i]))
            opers.append(expression[i])
            idx=i+1
    numbers.append(int(expression[idx:]))

    active_opers=list(set(opers))
    perm_opers=list(permutations(active_opers,len(active_opers)))
    for operators in perm_opers:
        tmp_numbers=deepcopy(numbers)
        tmp_opers=deepcopy(opers)
        for operator in operators:
            while operator in tmp_opers:
                idx=tmp_opers.index(operator)
                if operator=='+':
                    val=tmp_numbers[idx]+tmp_numbers[idx+1]
                elif operator=='-':
                    val = tmp_numbers[idx]- tmp_numbers[idx + 1]
                else:
                    val = tmp_numbers[idx] * tmp_numbers[idx + 1]

                if idx==0:
                    tmp_numbers=[val]+tmp_numbers[2:]
                elif idx==len(tmp_opers)-1:
                    tmp_numbers=tmp_numbers[0:idx]+[val]
                else:
                    tmp_numbers=tmp_numbers[0:idx]+[val]+tmp_numbers[idx+2:len(tmp_numbers)]
                tmp_opers.pop(idx)


        answer=max(answer,abs(tmp_numbers[0]))
    print(answer)
    return answer

solution("100-200*300-500+20")
solution("50*6-3*2")