def solution(x):
    
    str_x = str(x)
    result = sum([int(str_x[i]) for i in range(0, len(str_x))])
    
    return True if x%result==0 else False