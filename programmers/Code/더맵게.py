import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) >= 2:
            answer += 1
            num1 = heapq.heappop(scoville)
            num2 = heapq.heappop(scoville)
            heapq.heappush(scoville, num1 + (num2 * 2))
        else:
            if scoville[0] < K :
                break
        if scoville[0] >= K:
            return answer

    return -1

solution([1, 2, 3, 9, 10, 12],7)