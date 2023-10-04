def solution(left, right):
    result = 0
    
    
    for i in range(left, right+1):
        count = 0
        div_num = 1
        while div_num <= i:
            if i % div_num == 0:
                count += 1
            div_num += 1
        print(count)
        if count % 2 == 0:
            result += i
        else:
            result -= i
            
    return result