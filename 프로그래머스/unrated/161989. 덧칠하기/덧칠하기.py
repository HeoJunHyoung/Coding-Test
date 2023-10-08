def solution(n, m, section):
    
    result = 0
    
    while section:
        largest_range = section[0] + m
        while section and section[0] < largest_range:
            section.pop(0)
        result += 1
    
    return result
        