def solution(money):
    numberOfAmericano = money//5500;
    lastMoney = money%5500;
    result = []
    result.extend([numberOfAmericano, lastMoney])
    return result