import heapq

def solution(scoville, K):
    heap = sorted(scoville)
    
    cnt = 0
    while heap[0] < K:
        if len(heap) <= 1:
            break
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap)*2)
        cnt += 1
        
    return cnt if heap[0]>=K else -1