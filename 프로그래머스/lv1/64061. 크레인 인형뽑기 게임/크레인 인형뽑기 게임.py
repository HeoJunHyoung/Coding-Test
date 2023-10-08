def solution(board, moves):
    
    new_board = [[] for i in range(0,len(board))]
    result = 0
    stack = []
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            new_board[i].append(board[j][i])
            
    #print(new_board)
    
    for i in moves: # 1,5,3,5,1,2,1,4
        
        for j in range(len(new_board)): # 0 1 2 3 4
            
            if new_board[i-1][j] != 0:
                stack.append(new_board[i-1][j])
                new_board[i-1][j] = 0
                break
                
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                del stack[-1]
                del stack[-1]
                result += 2
            
    
    return result
        