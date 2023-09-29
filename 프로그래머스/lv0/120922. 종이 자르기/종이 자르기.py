def solution(M, N):
    
    mul1 = max(M, N) - 1
    mul2 = (min(M, N)-1) * max(M, N)
    return mul1 + mul2