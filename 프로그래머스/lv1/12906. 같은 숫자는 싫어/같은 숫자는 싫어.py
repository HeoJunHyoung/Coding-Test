def solution(arr):
    answer = []
    prev = arr[0]
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if prev == arr[i]:
            continue
        else:
            answer.append(arr[i])
        prev = arr[i]
    
    return answer