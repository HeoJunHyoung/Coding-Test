def solution(name, yearning, photo):
    answer = []
    
    for i in range(0, len(photo)): # 3
        total = 0
        for j in range(0, len(photo[i])): # 4
            for k in range(0, len(name)): # 4
                if name[k]==photo[i][j]:
                    total += yearning[k]
        answer.append(total)
        
    return answer