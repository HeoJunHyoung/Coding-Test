def solution(board, k):
    answer = 0
    for i in range(0, len(board)): # 0 1 2 3
        for j in range(0, len(board[i])): # 0 1 2
            if i+j <= k:
                answer += board[i][j]
    return answer