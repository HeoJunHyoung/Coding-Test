def solution(n, s):
    
    result = []
    
    if s<n:
        return [-1]
    
    if s%n==0:
        for i in range(n):
            result.append(s//n)
        return result
    else:
        rest = s % n
        for i in range(n):
            result.append(s//n)
        for i in range(rest):
            result[i] = result[i] + 1
        return sorted(result)