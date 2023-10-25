def solution(numbers):
    
    stack = []
    result = [0] * len(numbers)
    
    for index, value in enumerate(numbers):
        
        while stack and value > numbers[stack[-1]]:
            result[stack.pop()] = value
        stack.append(index)
        
    while stack:
        result[stack.pop()] = -1
    
    return result