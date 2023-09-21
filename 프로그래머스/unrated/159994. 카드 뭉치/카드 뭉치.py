def solution(cards1, cards2, goal):
    answer=''
    cards1_index = 0
    cards2_index = 0
    new_string = []
    for i in range(0, len(goal)):
        
        if goal[i] in cards1:
            if cards1.index(goal[i]) != 0:
                return 'No'
            new_string.append(goal[i])
            del cards1[cards1.index(goal[i])]
            cards1_index+=1
            
        elif goal[i] in cards2:
            if cards2.index(goal[i]) != 0:
                return 'No'
            new_string.append(goal[i])
            del cards2[cards2.index(goal[i])]
            cards2_index+=1

    if new_string == goal:
        answer = 'Yes'
        return answer
