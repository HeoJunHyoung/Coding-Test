from collections import deque

def solution(s):
    
    rotated = ''
    answer = 0
    
    if len(s)%2!=0:
        return 0
    
    for i in range(0, len(s)):
        count = 0
        rotated = s[i:] + s[0:i]
        dq = deque()
        for j in (s[i:] + s[0:i]):
            dq.append(j)
            if len(dq)>=2:
                if dq[-2]+dq[-1]=='[]' or dq[-2]+dq[-1]=='()' or dq[-2]+dq[-1]=='{}':
                    count += 1
                    dq.pop()
                    dq.pop()
        if count == len(s)//2:
            answer += 1
    
    return answer
                
        