def solution(n, left, right):
    
    answer = []
    
    # N*N배열에서 행과 열은 몫과 나머지로 일반화된다.
    for i in range(left, right+1):
        a = i//n
        b = i%n
        if a<b:
            a,b = b,a
        answer.append(a+1)
    
    return answer









#def solution(n, left, right):
    
    #arr = [[0]*n for i in range(n)]
    #result = []
    
    #for i in range(n):
        #for j in range(0, i+1):
            #arr[i][j] = i+1
            #arr[j][i] = i+1
            
    
    #result = sum(arr, [])
    
    #return result[left:right+1]
    
    
        