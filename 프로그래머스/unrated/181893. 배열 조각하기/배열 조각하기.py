def solution(arr, query):
    answer = []
    
    for index, value in enumerate(query):
        # If Index is even
        if index % 2 == 0:
            arr = arr[:value+1]
            
        # If Index is odd
        else:
            arr = arr[value:]
    
    
    return arr