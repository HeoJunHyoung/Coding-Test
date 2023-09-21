def solution(k, score):
    answer = []
    honor = []
    for index, value in enumerate(score):

        honor.append(value)
        
        if len(honor) <= k:
            honor = sorted(honor, reverse=True)
            answer.append(min(honor))
            
        else:
            honor = sorted(honor, reverse=True)
            answer.append(honor[k-1])
            del honor[honor.index(min(honor))]
    return answer
