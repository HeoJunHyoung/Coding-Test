def solution(myStr):
    answer = []
    temp = ''
    exclude_word = ['a','b','c']
    for i in myStr:
        if i in exclude_word:
            if temp != "":
                answer.append(temp)
            temp = ''
        else: temp+=i
    if temp != "":
        answer.append(temp)
    if not answer: return ["EMPTY"]
    return answer
    
            
    