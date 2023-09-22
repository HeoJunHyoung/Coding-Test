def solution(money):
    result = []
    result.extend([money//5500, money%5500])
    return result