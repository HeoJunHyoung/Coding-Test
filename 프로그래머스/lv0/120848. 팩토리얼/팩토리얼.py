def solution(n):
    
    result = 1
    start_num = 0
    
    while result <= n: # 6 < 7
        start_num += 1 # 4
        result = result * start_num # 2 * 3 = 6
    
    return start_num - 1