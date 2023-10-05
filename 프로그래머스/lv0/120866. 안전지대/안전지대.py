def solution(board):
    
    newList = [[0]*len(board) for i in range(len(board))]
    zero_count = 0
    
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == 1:
                for k in range(max(0, i-1), min(i+2, len(board))):
                    for l in range(max(0, j-1), min(j+2, len(board))):
                        # print(k, l)
                        newList[k][l] = 1
    
    for i in range(len(board)):
        zero_count += newList[i].count(0)
    return zero_count

        