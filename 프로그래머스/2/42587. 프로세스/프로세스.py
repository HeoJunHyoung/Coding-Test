from collections import deque

def solution(priorities, location):
    
    dq = deque(priorities)
    processing_count = 0
    
    while location >= 0:
        
        ready = dq.popleft()
        if not dq:
            processing_count += 1
            break
        location -= 1
        
        if ready < max(dq):
            if location == -1:
                location += len(dq) + 1
            dq.append(ready)
        else:
            processing_count += 1
    
    return processing_count
            
        