from collections import deque

def solution(people, limit):
    
    boat_count = 0
    people = sorted(people)
    dq = deque(people)
    
    while dq:
        if dq[0] + dq[-1] > limit:
            dq.pop()
            boat_count += 1
        else:
            if len(dq) < 2:
                dq.pop()
            elif len(dq) >= 2:
                dq.popleft()
                dq.pop()
        
            boat_count += 1
    return boat_count
    
                