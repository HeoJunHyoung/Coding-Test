import heapq

def solution(scoville, K):
    blend_count = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        
        blend_count += 1
        
        min_one = heapq.heappop(scoville)
        min_two = heapq.heappop(scoville)
        
        heapq.heappush(scoville, min_one + (min_two*2))
        
        if len(scoville)==2 and (scoville[0]+scoville[1]*2) < K:
            return -1
        
    
    return blend_count
    
    
        
    
    