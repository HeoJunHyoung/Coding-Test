from collections import deque
import sys
input = sys.stdin.readline

def dfs(adj_list, visited, s):

    stack = deque([s])

    while stack:
        current = stack.popleft()
        if not visited[current]:
            visited[current] = True
        
        for n in adj_list[current]:
            if not visited[n]:
                stack.append(n)
                visited[n] = True

node, edge = map(int, input().split())
adj_list = [[] for _ in range(node+1)]

for i in range(edge):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

visited = [False] * (node + 1)
count = 0

for i in range(1, node+1):
    if not visited[i]:
        dfs(adj_list, visited, i)
        count += 1

print(count)