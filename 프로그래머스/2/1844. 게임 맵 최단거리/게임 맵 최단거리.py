from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    queue = deque([(0, 0, 1)])

    while queue:
        r, c, dist = queue.popleft()

        if r == n - 1 and c == m - 1:
            return dist

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                queue.append((nr, nc, dist + 1))

    return -1