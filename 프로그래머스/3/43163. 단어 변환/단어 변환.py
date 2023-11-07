from collections import deque

def solution(begin, target, words):
    
    stack = [(begin, 0)]
    dq = deque(stack)
    visited = [False] * len(words)
    
    if target not in words:
        return 0
    
    while dq:
        
        cur_word, depth = dq.popleft()
        
        if cur_word == target:
            return depth
        
        for i in range(len(words)):
            diff = 0
            for j in range(len(words[i])):
                if cur_word[j] != words[i][j]:
                    diff += 1
            if diff == 1 and not visited[i]:
                visited[i] = True
                dq.append((words[i], depth+1))
        
        print(dq)
                
    return 0
        
        