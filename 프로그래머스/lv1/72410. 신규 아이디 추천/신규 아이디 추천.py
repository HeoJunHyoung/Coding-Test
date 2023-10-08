def solution(new_id):
    
    # 1단계
    new_id = new_id.lower()
    print(new_id)
    
    answer = ''
    # 2단계
    for word in new_id:
        if word.isalpha() or word.isnumeric() or word in '-_.':
            answer += word
    print(answer)
    
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    print(answer)
    
    
    # 4단계
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    print(answer)
    
    # 5단계
    if not answer:
        answer = 'a'
    print(answer)
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]
    print(answer)
    
    # 7단계
    if len(answer) <= 2:
        for i in range(0, 3-len(answer)):
            answer += answer[-1]
    print(answer)
    
    return answer