def solution(numbers, hand):
    answer = ''
    
    left = [3,0]
    right = [3,2]
    
    left_only = [1,4,7]
    right_only = [3,6,9]
    
    numbers_location = dict(zip(list(range(1,10)), [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]))
    numbers_location[0] = [3,1]
    
    #print(numbers_location)
    
    for i in range(len(numbers)):
        if numbers[i] in left_only:
            left = numbers_location[numbers[i]]
            print(left)
            answer += 'L'
        elif numbers[i] in right_only:
            right = numbers_location[numbers[i]]
            answer += 'R'
        else:
            push = numbers_location[numbers[i]]
            left_move = abs(push[0]-left[0]) + abs(push[1]-left[1])
            right_move = abs(push[0]-right[0]) + abs(push[1]-right[1])
            if left_move < right_move:
                left = push
                answer += 'L'
            elif left_move > right_move:
                right = push
                answer += 'R'
            else:
                if hand=='right':
                    right = push
                    answer += 'R'   
                else:
                    left = push
                    answer += 'L'
            
        
    
    
    
    return answer