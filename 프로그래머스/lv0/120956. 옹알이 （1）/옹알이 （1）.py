def solution(babbling):
    
    speakable_word = ["aya", "ye", "woo", "ma"]
    result = 0
    
    for i in range(len(babbling)):
        for j in range(len(speakable_word)):
            if speakable_word[j] in babbling[i]:
                babbling[i] = babbling[i].replace(speakable_word[j], ' ')
        babbling[i] = babbling[i].replace(' ', '')
        
    for i in range(0, len(babbling)):
        if not babbling[i].isalpha():
            result += 1
    return result