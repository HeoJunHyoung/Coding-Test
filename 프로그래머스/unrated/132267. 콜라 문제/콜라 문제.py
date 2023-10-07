def solution(a, b, n):
    
    total = n
    new_cola = 0
    
    while total >= a:
        new_cola = new_cola + total // a * b
        total = (total // a * b) + (total % a)
    
    return new_cola
    