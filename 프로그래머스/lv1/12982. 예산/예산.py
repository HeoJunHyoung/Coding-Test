def solution(d, budget):
    
    spent_money = 0
    result = 0
    d = sorted(d)
    
    # 최소금액이 예산보다 큰 경우는 아무것도 살 수 없음
    if d[0] > budget:
        return 0
    
    for i in d:
        if spent_money > budget:
            result -= 1
            break
        elif spent_money == budget:
            break
        else:
            spent_money += i
            result += 1
    
    return result



