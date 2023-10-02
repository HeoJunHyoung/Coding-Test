def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        #print(s,e,k)
        min = 1000000000
        for i in range(s, e+1):
            # print(i)
            if arr[i] > k:
                if min>arr[i]:
                    min = arr[i]
        if min == 1000000000:
            answer.append(-1)
        else:
            answer.append(min)
    
    return answer
    