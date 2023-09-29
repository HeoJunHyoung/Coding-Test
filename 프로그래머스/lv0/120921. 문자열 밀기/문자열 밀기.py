def solution(A, B):
    
    if A==B:
        return 0
    else:
        for i in range(0, len(A)):
            A = A[-1] + A[0:len(A)-1]
            if A == B:
                return i+1
        
    return -1
    