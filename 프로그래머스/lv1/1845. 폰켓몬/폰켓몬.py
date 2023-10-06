def solution(nums):
    
    pick_number = len(nums)//2
    
    nums = set(nums)
    
    if len(nums) > pick_number:
        return pick_number
    else:
        return len(nums)