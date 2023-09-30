def solution(bin1, bin2):
    answer = ''
    
    len1, len2 = len(bin1), len(bin2)
    jisoo1, jisoo2 = len1 - 1, len2 - 1
    result1, result2, total = 0, 0, 0
    
    for i in range(0, len1):
        result1 += 2**jisoo1 * int(bin1[i])
        jisoo1 -= 1
        
    for i in range(0, len2):
        result2 += 2**jisoo2 * int(bin2[i])
        jisoo2 -= 1
        
    total = result1 + result2
    
    jisoo = 1
    while total >= 2**jisoo:
        jisoo += 1
    jisoo -= 1
    
    for i in range(0, jisoo + 1):
        answer += str(total // 2**jisoo)
        total = total % 2**jisoo
        jisoo -= 1
        
    return answer