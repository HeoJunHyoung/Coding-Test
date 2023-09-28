def solution(order):

# 아메리카노 -> 4500
# 카페 라테 -> 5000

# 메뉴만 -> 차가운것
# 아무거나 -> 차가운것 + 아메리카노

    price = 0
    for i in range(0, len(order)):
        if order[i] == 'anything':
            price += 4500
        else:
            if 'americano' in order[i]:
                price += 4500
            else:
                price += 5000
    
    return price