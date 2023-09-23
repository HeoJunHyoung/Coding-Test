def solution(numbers, n):
    
    sum = 0
    
    for i in numbers:
        if sum > n:
            return sum
        else:
            sum += i
    
    return sum