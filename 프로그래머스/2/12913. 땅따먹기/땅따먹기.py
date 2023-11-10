def solution(land):
    
    for i in range(len(land)-1):
        for j in range(4):
            land[i+1][j] = max(land[i][:j] + land[i][j+1:]) + land[i+1][j]
    
    return max(max(land))