def solution(msg):
    
    dictionary = dict(zip([chr(i) for i in range(ord('A'), ord('Z')+1)], [i for i in range(1, 27)]))
    #print(dictionary)
    
    answer = []
    i = 0
    
    while i < len(msg):
        common_word = ''
        common_index = 0
        for j in range(i+1, len(msg)+1):
            if msg[i:j] in dictionary:
                common_word = msg[i:j]
                common_index = j
    
        answer.append(dictionary[common_word])
        if common_index < len(msg):
            temp = common_word + msg[common_index]
            dictionary[temp] = len(dictionary) + 1
        else:
            temp = msg[common_index-1]
            dictionary[temp] = len(dictionary) + 1

        
        i = i + (common_index - i)
    
    return answer