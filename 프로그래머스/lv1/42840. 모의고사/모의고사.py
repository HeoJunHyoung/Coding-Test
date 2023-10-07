def solution(answers):
    
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    result = [0, 0, 0]
    newList = []
    
    for i in range(0, len(answers)):
        if answers[i] == stu1[i%len(stu1)]:
            result[0] += 1
        if answers[i] == stu2[i%len(stu2)]:
            result[1] += 1
        if answers[i] == stu3[i%len(stu3)]:
            result[2] += 1
    
    # print(result)
    
    for i in range(len(result)):
        if result[i] == max(result):
            newList.append(i+1)
            
    return sorted(newList)
            
    
    