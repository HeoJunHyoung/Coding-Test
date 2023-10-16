def findStartPoint(park):
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                return i, j

def solution(park, routes):
    
    x, y = findStartPoint(park)
    # print(x, y)
    
    # E / W -> y값 변경
    # E:(+) / W:(-)
    
    # N / S -> x값 변경
    # S:(+) / N:(-)
    
    for i in range(len(routes)):
        direc = routes[i][0]
        move = int(routes[i][-1])
        flag = True
        
        if direc == 'E':
            for j in range(1, move+1):
                if y + j >= len(park[0]) or park[x][y+j] == 'X' or y+j < 0:
                    flag = False
                    break
            if flag == True:
                y = y + move
                
        elif direc == 'W':
            for j in range(1, move+1):
                if y - j < 0 or park[x][y-j] == 'X' or y-j < 0:
                    flag = False
                    break
            if flag == True:
                y = y - move
                
        elif direc == 'S':
            for j in range(1, move+1):
                if x + j >= len(park) or park[x+j][y] == 'X' or x+j < 0:
                    flag = False
                    break
            if flag == True:
                x = x + move
        else:
            for j in range(1, move+1):
                if x - j > len(park) or park[x-j][y] == 'X' or x-j < 0:
                    flag = False
                    break
            if flag == True:
                x = x - move
                
    return [x, y]
            
        
        
        
        
        
        
        
        
        