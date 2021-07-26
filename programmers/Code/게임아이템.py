import heapq
from collections import deque
def solution(healths, items):
    answer = []
    max_heap = []
    items = deque(sorted([(item[1], item[0], idx+1) for idx,item in enumerate(items)]))

    healths.sort()
    for health in healths :
        while items and health - items[0][0] >= 100:
            item = items.popleft()
            heapq.heappush(max_heap,(-item[1], item[2]))
        if max_heap:
            answer.append(heapq.heappop(max_heap)[1])
    return sorted(answer)

solution([200,120,150],[[30,100],[500,30],[100,400]])
solution([300,200,500],[[1000, 600], [400, 500], [300, 100]])