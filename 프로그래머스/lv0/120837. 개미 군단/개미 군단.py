def solution(hp):
    # 장군:5 병정:3 일:1
    ant_num = 0
    
    while hp != 0:
        if hp>=5: 
            hp = hp-5
            ant_num+=1
        elif hp>=3: 
            hp = hp-3
            ant_num+=1
        else:
            hp = hp-1
            ant_num+=1
    
    return ant_num
    