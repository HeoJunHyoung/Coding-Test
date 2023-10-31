def solution(numbers):
    
    numbers = list(map(str, numbers))    
    sorted_numbers = sorted(numbers, reverse=True, key = lambda x : x * 3)
    #print(sorted_numbers)
    #return ''.join(sorted_numbers)
    return str(int(''.join(sorted_numbers)))
    
    