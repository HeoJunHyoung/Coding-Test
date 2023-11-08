def findJari(n):
    total = 0
    i = 1
    while True:
        total = total + 3**(i)# 3
        if n < total+1:
            break
        i += 1
    return i

def solution(n):
    
    jari= findJari(n)
    special_number = [1,2,4]
    result = ''
    for j in range(jari, 0, -1):
        mok, rest = divmod(n-1, 3)
        result += str(special_number[rest])
        n = mok
        
    return result[::-1]
    
    
    
    
        