def solution(numbers, hand):
    def cal(a,b):
        return abs(a[0]-b[0])+abs(a[1]-b[1])
    answer = ''
    phone = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1]
    }

    left, right = [3, 0], [3, 2]
    for number in numbers:
        if number==1 or number==4 or number==7:
            answer+='L'
            left=phone[number]
        elif number==3 or number==6 or number==9:
            answer+='R'
            right=phone[number]
        else:
            dist_left=cal(left,phone[number])
            dist_right=cal(right,phone[number])
            if dist_left<dist_right:
                answer += 'L'
                left = phone[number]
            elif dist_left>dist_right:
                answer += 'R'
                right = phone[number]
            else:
                if hand=='left':
                    answer += 'L'
                    left = phone[number]
                else:
                    answer += 'R'
                    right = phone[number]
    print(answer)
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right')
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	,'left')
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],'right')
