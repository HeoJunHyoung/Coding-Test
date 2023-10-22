def gcd(n1, n2):
    # 큰 수를 n1, 작은 수를 n2로 고정
    if n2>n1:
        n1,n2 = n2,n1
    if n2==0:
        return n1
    else:
        return gcd(n2, n1%n2)


def solution(arr):
    
    criterion = arr[0] * arr[1] / gcd(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        criterion = criterion * arr[i] / gcd(criterion, arr[i])
    
    return criterion