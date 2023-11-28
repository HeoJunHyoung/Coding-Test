def solution(numbers, target):
    
    stack = [[0, 0, 0]] # idx, total, depth
    cnt = 0
    
    while stack:
        idx, total, depth = stack.pop()
        if depth == len(numbers) and total == target:
            cnt += 1
            continue
            
        if depth < len(numbers):
            stack.append([idx+1, total + numbers[idx], depth + 1])
            stack.append([idx+1, total - numbers[idx], depth + 1])
            idx += 1
    
    return cnt