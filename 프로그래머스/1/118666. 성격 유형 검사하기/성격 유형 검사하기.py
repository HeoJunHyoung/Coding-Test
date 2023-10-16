def solution(survey, choices):
    
    choices = [i-1 for i in choices]
    alpha_score = dict(zip(['R','T','C','F','J','M','A','N'], [0]*8))
    answer = ''
    #print(alpha_score)
    
    for index, choice in enumerate(choices):
        if choice == 3:
            continue
        elif choice < 3:
            score = 3 - choice
            alpha_score[survey[index][0]] += score
        else:
            score = choice - 3
            alpha_score[survey[index][-1]] += score
            
    #print(alpha_score)
    
    # 1
    if alpha_score['R'] > alpha_score['T']:
        answer += 'R'
    elif alpha_score['R'] < alpha_score['T']:
        answer += 'T'
    else:
        answer += 'R'
        
    #2 
    if alpha_score['C'] > alpha_score['F']:
        answer += 'C'
    elif alpha_score['C'] < alpha_score['F']:
        answer += 'F'
    else:
        answer += 'C'
        
    # 3
    if alpha_score['J'] > alpha_score['M']:
        answer += 'J'
    elif alpha_score['J'] < alpha_score['M']:
        answer += 'M'
    else:
        answer += 'J'
    
    # 4
    if alpha_score['A'] > alpha_score['N']:
        answer += 'A'
    elif alpha_score['A'] < alpha_score['N']:
        answer += 'N'
    else:
        answer += 'A'
        
    
    return answer
    
    