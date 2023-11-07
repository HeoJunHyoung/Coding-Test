def solution(dirs):
    
    direction_list = []
    
    before = [0, 0]
    after = [0, 0]
    cnt = 0
    
    for direction in dirs:
        if direction == 'U':
            if before[1]+1 > 5:
                continue
            after = [before[0], before[1]+1]
                     
        elif direction == 'D':
            if before[1]-1 < -5:
                continue
            after = [before[0], before[1]-1]
        
        elif direction == 'R':
            if before[0]+1 > 5:
                continue
            after = [before[0]+1, before[1]]
            
        elif direction == 'L':
            if before[0]-1 < -5:
                continue
            after = [before[0]-1, before[1]]
                     
        
        
        if before+after not in direction_list:
            direction_list.append(before+after)
            direction_list.append(after+before)
            cnt += 1
        
        before = after
    
    print(direction_list)
    return cnt
        
        
            