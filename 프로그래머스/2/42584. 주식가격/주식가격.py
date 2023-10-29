from collections import deque

def solution(prices):
    
    dq = deque(prices)
    answer = []
    
    while dq:
        cnt = 0
        current = dq.popleft()
        for d in dq:
            cnt += 1
            if current > d:
                break
        answer.append(cnt)
    
    return answer