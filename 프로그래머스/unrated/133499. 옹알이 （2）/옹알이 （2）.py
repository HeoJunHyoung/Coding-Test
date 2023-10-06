def solution(babbling):
    
    word = ["aya", "ye", "woo", "ma"]
    speakable_count = 0
    speakable_list = []
    
    for i in range(len(babbling)):
        for j in range(len(word)):
            babbling[i] = babbling[i].replace(word[j], str(word.index(word[j])))
        
    #print(babbling)
    for item in babbling:
        if item.isnumeric():
            speakable_list.append(str(item))
            speakable_count += 1
    
    print(speakable_list)
    
    for i in range(0, len(speakable_list)):
        flag = 0
        for j in range(0, len(speakable_list[i])-1):
            if speakable_list[i][j] == speakable_list[i][j+1]:
                flag = 1
        if flag == 1:
            speakable_count -= 1
    
    return speakable_count
                