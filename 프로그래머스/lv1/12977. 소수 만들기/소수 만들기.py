def findPrime(n):
    count = 0
    for i in range(1, n+1):
        if n % i ==0:
            count += 1
    return True if count==2 else False

def solution(nums):
    
    sum = 0
    result = 0
    
    for i in range(0, len(nums)-2): # 0 1 2 3 4 5
        for j in range(i+1, len(nums)-1): # 1 2 3 4
            for k in range(j+1, len(nums)): # 2 3 4 5
                # print(i, j, k)
                sum = nums[i] + nums[j] + nums[k]
                if findPrime(sum):
                    result += 1
    return result
                
            
        
    


    