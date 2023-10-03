def solution(n):
    arr = [[0*n]*n for i in range(n)]
    start_index = 0
    end_index = n-1
    count = 1
    
    while start_index < end_index:
        
        ## Part 1
        for i in range(start_index, end_index+1):
            arr[start_index][i] = count
            count += 1
        #print('1')
        #print(arr)
        
        count -=1
        ## Part 2
        for i in range(start_index, end_index+1):    
            arr[i][end_index] = count
            count += 1
        #print('2')    
        #print(arr)
        
        ## Part 3
        for i in range(end_index-1, start_index-1, -1):
            arr[end_index][i] = count
            count += 1
        #print('3')
        #print(arr) 
        
        ## Part 4
        for i in range(end_index-1, start_index, -1):
            #print(i)
            arr[i][start_index] = count
            count += 1
        #print('4')
        #print(arr)
        
        start_index += 1
        end_index -= 1
    
    center_index = n // 2
    if arr[center_index][center_index] == 0:
        arr[center_index][center_index] = n*n
        
    return arr
    
    
    
    
    