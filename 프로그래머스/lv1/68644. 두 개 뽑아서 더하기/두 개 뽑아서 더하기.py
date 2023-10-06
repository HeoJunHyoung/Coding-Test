def solution(numbers):
    
    answer = []
    
    
    for i in range(0, len(numbers)):
        sum = 0
        for j in range(i+1, len(numbers)):
            sum = numbers[i]+numbers[j]
            #print(sum)
            if sum not in answer:
                answer.append(sum)
    
    return sorted(answer)