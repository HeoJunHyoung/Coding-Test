def solution(A, B):
    
    A, B = sorted(A, reverse=True), sorted(B, reverse=True)
    count = 0
    
    for i in A:
        if i < B[0]:
            del B[0]
            count += 1
        else:
            continue
    
    return count