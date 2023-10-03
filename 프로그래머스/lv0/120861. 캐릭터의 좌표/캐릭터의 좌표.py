def solution(keyinput, board):
    
    board[0], board[1] = board[1], board[0]
    #print(board)
    
    center = [board[0]//2, board[1]//2]
    start = [0, 0]
    #print(center)
    
    leftLimit = -center[1]
    rightLimit = center[1]
    upLimit = center[0]
    downLimit = -center[0]
    print(leftLimit, rightLimit, upLimit, downLimit)
    
    
    for input in keyinput:
        if input == 'left':
            if start[0] - 1 > leftLimit:
                start[0] -= 1
            else:
                start[0] = leftLimit
        
        elif input == 'right':
            if start[0] + 1 < rightLimit:
                start[0] += 1
            else:
                start[0] = rightLimit
                
        elif input == 'up':
            if start[1] + 1 < upLimit:
                start[1] += 1
            else:
                start[1] = upLimit
        else:
            if start[1] - 1 > downLimit:
                start[1] -= 1
            else:
                start[1] = downLimit
                
    return start
    
    
    
            
            
            
            
            
            
            
            
            
            