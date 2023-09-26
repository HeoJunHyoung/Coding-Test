def solution(price):
    
    
    if price - 500000 >= 0:
        return int(price * 0.8)
    elif price - 300000 >= 0:
        return int(price * 0.9)
    elif price - 100000 >= 0:
        return int(price * 0.95)
    else:
        return price
    