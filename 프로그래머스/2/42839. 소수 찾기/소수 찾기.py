from itertools import combinations
from itertools import permutations

def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    cnt = 0
    cases = []
                     
    for i in range(1, len(numbers)+1):
        for pick in permutations(numbers, i):
            cases.append(''.join(pick))
    
    cases = list(set([int(i) for i in cases]))
    
    
    for case in cases:
        if isPrime(int(case)):
            cnt += 1
    
    return cnt
    