def solution(common):
    
    # 등차수열인 경우
    if common[1]-common[0] == common[2]-common[1]:
        a = common[0]
        d = common[1]-common[0]
        return a+((len(common))*d)
    else:
        a = common[0]
        r = common[1]/common[0]
        return a*r**(len(common))