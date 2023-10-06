def solution(number):
    
    result = 0
    
    for i in range(0, len(number)-2): # 0 1 2 3 4  
        for j in range(1, len(number)-1): # 1 2 3 4 5
            for k in range(2, len(number)): # 2 3 4 5 6
                if i<j and j<k:
                    #print('i:{} j:{} k:{}'.format(i,j,k))
                    if number[i]+number[j]+number[k] == 0:
                        #print(number[i], number[j], number[k], i, j, k)
                        result += 1
    
    return result
    