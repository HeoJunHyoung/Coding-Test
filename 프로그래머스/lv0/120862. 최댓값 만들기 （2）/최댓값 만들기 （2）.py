def solution(numbers):
    
    
    sorted = numbers.sort()
    plusResult = numbers[-1]*numbers[-2]
    minusResult = numbers[0]*numbers[1]
    
    return plusResult if plusResult>minusResult else minusResult