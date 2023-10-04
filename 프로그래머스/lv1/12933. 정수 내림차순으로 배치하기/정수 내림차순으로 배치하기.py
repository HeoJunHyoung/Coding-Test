def solution(n):
    
    n = str(n)
    return int(''.join(sorted([n[i] for i in range(0, len(n))], reverse=True)))