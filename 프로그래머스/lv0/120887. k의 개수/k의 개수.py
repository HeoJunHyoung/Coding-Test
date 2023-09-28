def solution(i, j, k):
    
    listX = [str(i) for i in range(i, j+1)]
    count = 0
    
    for x in range(len(listX)):
        for y in range(len(listX[x])):
            # print(y)
            if listX[x][y] == str(k):
                count += 1
    
    return count