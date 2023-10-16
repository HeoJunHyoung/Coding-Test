def isPrime(n):
    
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True


def solution(n):
    
    answer = 0
    num_list = [i for i in range(2, n+1)]
    for num in num_list:
        if isPrime(num):
            answer += 1
    return answer