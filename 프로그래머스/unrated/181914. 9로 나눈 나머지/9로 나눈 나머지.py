def solution(number):
    
    result = 0
    for i in range(0, len(number)):
        result += int(number[i])
    
    return result%9