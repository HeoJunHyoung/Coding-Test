
def solution(numbers, target):
    
    # 스택 자체에 깊이와 누적 값을 넣음
    stack=[[0, 0]]
    count = 0
    
    while stack:
        current_depth, current_sum = stack.pop()
        
        if current_depth == len(numbers) and current_sum == target:
            count += 1
        
        else:
            if current_depth < len(numbers):
                stack.append([current_depth+1, current_sum + numbers[current_depth]])
                stack.append([current_depth+1, current_sum - numbers[current_depth]])
        
    
    return count
