def solution(want, number, discount):
    
    day_discount = []
    want_number = dict(zip(want, number))
    result = 0
    
    for i in range(0, len(discount)-sum(number)+1): # 0 1 2 3 4
        flag = True
        day_discount = discount[i:i+sum(number)]
        #print(day_discount)
        for fruit in want:
            if want_number[fruit] > day_discount.count(fruit):
                flag = False
        if flag==True:
            result += 1
    
    return result
                    
        
                