def solution(m, n, board):
    board = [list(board[i]) for i in range(m)]
    cnt = 0

    while True:
        delete_index = set()

        for i in range(m - 1):
            for j in range(n - 1):
                target = board[i][j]
                if target == '#':
                    continue
                if target == board[i][j + 1] and target == board[i + 1][j] and target == board[i + 1][j + 1]:
                    delete_index.add((i, j))
                    delete_index.add((i, j + 1))
                    delete_index.add((i + 1, j))
                    delete_index.add((i + 1, j + 1))

        # 4블록으로 연결된 블록이 없으면 반복문 탈출
        if not delete_index:
            break

        # 블록 삭제 표시
        for r, c in delete_index:
            board[r][c] = '#'

        # 삭제된 블록 수 증가
        cnt += len(delete_index)

        # 빈 공간을 블록 위로 올리기
        for j in range(n):
            col = [board[i][j] for i in range(m) if board[i][j] != '#']
            col = ['#'] * (m - len(col)) + col
            for i in range(m):
                board[i][j] = col[i]

    return cnt