def solution(arr):
    
    row, col = len(arr), len(arr[0])
    
    if row==col:
        return arr
    elif row > col:
        for i in range(0, row):
            for j in range(0, row-col):
                arr[i].append(0)
    else:
        for i in range(0, col-row):
            arr.append([0]*col)
            
    return arr