def solution(num, total):
    
    result = []
    
    center = total // num
    boundary = num // 2
    
    print(center, boundary)
    
    for i in range(center-boundary, center+boundary+1):
        result.append(i)
    
    if sum(result)==total:
        return result
    else:
        result1 = result[1:]
        result2 = result[:-2]
        if sum(result1) == total:
            del result[0]
            return result
        else:
            del result[-1]
            return result