def dfs(adj_list, visited, start):

    stack = [start]
    
    while stack:
        print(stack)
        current = stack.pop()
        visited[current] = True
        
        for value in adj_list[current]:
            if not visited[value]:
                stack.append(value)
    
    return visited
    
    
    
    
    
def solution(n, computers):
    
    # 인접 행렬 -> 인접 리스트 변환 작업
    adj_list = [[] for _ in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i==j:
                continue
            if computers[i][j] == 1:
                adj_list[i].append(j)
    
    visited = [False] * (n)
    count = 0
    
    for i in range(n): # 0 1 2
        if not visited[i]:
            visited = dfs(adj_list, visited, i)
            count += 1
            
    return count
    