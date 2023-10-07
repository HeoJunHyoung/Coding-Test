def solution(food):
    
    ans1 = ''
    ans2 = ''
    
    for i in range(1, len(food)):
        eat_number = food[i] // 2
        eat_index = i
        for j in range(eat_number):
            ans1 = ans1 + str(eat_index)
            ans2 = str(eat_index) + ans2
    
    return ans1+'0'+ans2