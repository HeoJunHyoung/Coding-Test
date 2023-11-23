from collections import deque

def solution(people, limit):
    result = 0
    
    dq = deque(sorted(people, reverse=True))
    print(dq)
    while dq:
        if dq[0] + dq[-1] <= limit:
            result += 1
            dq.popleft()
            if len(dq) == 0:
                break
            dq.pop()
        else:
            result += 1
            dq.popleft()
    
    return result