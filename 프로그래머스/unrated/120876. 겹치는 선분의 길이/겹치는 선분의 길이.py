def solution(lines):
    
    line_dict = dict(zip(list(range(-100, 101)), [0]*201))
    #print(line_dict)    
    for i in range(len(lines)):
        for j in range(lines[i][0], lines[i][1]):
            line_dict[j] += 1
    
    count = 0
    
    for value in line_dict.items():
        if value[1] >= 2:
            count += 1
    return count
            
            
    
