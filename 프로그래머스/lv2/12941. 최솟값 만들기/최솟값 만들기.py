def solution(A,B):
    
    result = 0
    
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    return sum([A[i]*B[i] for i in range(len(A))])