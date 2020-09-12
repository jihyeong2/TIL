from itertools import combinations
def solution(orders, course):
    answer = []
    orders_length=len(orders)
    order_comb_list=[[] for _ in range(10)]
    for order_idx in range(orders_length):
        for comb_length in range(2,len(orders[order_idx])+1):
            order_comb=combinations(sorted(orders[order_idx]),comb_length)
            for combs in order_comb:
                tmp=''
                for x in combs:
                    tmp+=x
                order_comb_list[comb_length-2].append(tmp)
    # print(order_comb_list)
    for c in course:
        max_cnt=0
        for sub_course in order_comb_list[c-2]:
            # print(c,sub_course,order_comb_list[c-2].count(sub_course))
            if order_comb_list[c-2].count(sub_course)<2: continue
            if order_comb_list[c-2].count(sub_course)>max_cnt:
                max_cnt=order_comb_list[c-2].count(sub_course)
        for sub_course in order_comb_list[c - 2]:
            if order_comb_list[c-2].count(sub_course)==max_cnt and sub_course not in answer:
                answer.append(sub_course)

    answer.sort()
    return answer
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))