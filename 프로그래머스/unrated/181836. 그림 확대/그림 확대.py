def solution(picture, k):
    answer = []
    
    for i in range(0, len(picture)):
        string = ''
        for j in range(0, len(picture[i])):
            for m in range(0, k): # 0 1
                string += picture[i][j]
        for index in range(0, k):
            answer.append(string) 
    
    
    
    
    return answer