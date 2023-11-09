'''
DFS 혹은 BFS로 풀 수 있을것으로 보임.

'''

def dfs(maps, r, c):
    
    stack = [[r, c]]
    total = 0
    
        # 우 좌 상 하
    dr = [0, 0,-1,1]
    dc = [1,-1, 0,0]
    
    while stack:
        
        r, c = stack.pop()
        total += int(maps[r][c])
        maps[r][c] = 'X'
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if nr < 0 or nc < 0 or nr > len(maps)-1 or nc > len(maps[0])-1:
                continue
                
            if maps[nr][nc] == 'X' or [nr, nc] in stack:
                continue
            else:
                stack.append([nr, nc])
    
    return maps, total
    
                   
    
def solution(maps):
       
    maps = [list(map(str, maps[i])) for i in range(len(maps))]
    #print(maps)
    result = []
    
    for r in range(len(maps)):
        for c in range(len(maps[r])):
            if maps[r][c] == 'X':
                continue
            else:
                maps, day = dfs(maps, r, c)
                result.append(day)
    
    return sorted(result) if result else [-1]
    