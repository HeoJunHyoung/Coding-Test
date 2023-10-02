def solution(arr):
    
    prev = [0]*len(arr)
    count = 0
    
    while prev != arr:
        
        prev = arr[:]
        
        for i in range(0, len(arr)):
            if arr[i]>=50 and arr[i]%2==0:
                arr[i] = arr[i] // 2
            elif arr[i]<50 and arr[i]%2!=0:
                arr[i] = arr[i]*2 + 1
        count += 1
        
        if prev == arr:
            return count - 1
    
            
        
        
        
        
        
    
    