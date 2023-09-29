def solution(l, r):
    answer = []
    exclude = ['1','2','3','4','6','7','8','9']
    
    for i in range(l, r+1):
        count = 0
        for j in range(0, len(str(i))): # 2
            if str(i)[j] not in exclude: 
                count += 1
                if count == len(str(i)):
                    answer.append(str(i))
    
    return sorted(map(int, answer)) if answer else [-1]