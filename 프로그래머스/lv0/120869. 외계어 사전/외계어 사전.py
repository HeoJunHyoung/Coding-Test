def solution(spell, dic):
    
    noDupleDic = []
    count = 0
    
    for i in range(0, len(dic)):
        setA = ''.join(set(dic[i]))
        noDupleDic.append(setA)

    # print(noDupleDic)
    
    for i in range(0, len(noDupleDic)):
        count = 0
        for j in range(0, len(noDupleDic[i])):
            if noDupleDic[i][j] in spell:
                count += 1
        if count == len(spell):
            return 1
    return 2