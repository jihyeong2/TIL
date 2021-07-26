import heapq
def solution(no, works):
    max_heap = []
    result = 0
    for work in works:
        heapq.heappush(max_heap, -work)
    for _ in range(no):
        if max_heap:
            work = heapq.heappop(max_heap)
            if work + 1 >= 0: continue
            heapq.heappush(max_heap, work+1)
    for work in max_heap:
        result += work**2
    return result
solution(4,[4,3,3])
solution(2,[3,3,3])