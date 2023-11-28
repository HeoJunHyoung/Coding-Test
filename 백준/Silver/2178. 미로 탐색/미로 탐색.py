import sys
from collections import deque

def bfs(maze, n, m, dq, visited):
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    while dq:
        r, c, depth = dq.popleft()

        if r == n-1 and c == m-1:
            return depth

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                dq.append([nr, nc, depth+1])

# Input
n, m = map(int, input().split())
maze = []

for i in range(n):
    x = input()
    x = [int(i) for i in x if i.isnumeric()]
    maze.append(x)

# Initialize the queue with the starting position (0, 0) and depth 1
dq = deque([[0, 0, 1]])

# Initialize the visited matrix
visited = [[False] * m for _ in range(n)]
visited[0][0] = True

# Call the BFS function and print the result
result = bfs(maze, n, m, dq, visited)
print(result)