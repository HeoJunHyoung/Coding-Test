import heapq

def solution(n, works):
    
    works = [-i for i in works]
    heapq.heapify(works)
    result = 0
    
    total = sum([i for i in works])
    if (-total) - n < 0:
        return 0
    
    while n>0:
        priority_pop = -heapq.heappop(works) - 1
        heapq.heappush(works, -priority_pop)
        n -= 1
    
    for i in range(len(works)):
        result = result + works[i]**2
    return result 