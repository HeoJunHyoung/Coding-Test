def solution(arr, flag):
    answer = []
    
    for i in range(0, len(flag)):
        if flag[i] == True:
            for j in range(0, arr[i]):
                answer.append(arr[i])
                answer.append(arr[i])
        else:
            for j in range(0, arr[i]):
                answer.pop()   
    
    
    return answer