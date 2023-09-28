def solution(numbers, k):
    
    current_index = 0
    
    
    while k-1 >= 0:
        
        current_index += 2
        if current_index >= len(numbers):
            current_index -= len(numbers)
        print(numbers[current_index])
        k -=1
    
    return numbers[current_index - 2]
    
    
        