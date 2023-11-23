def solution(n, words):
    result = []
    
    before = words[0][0]
    word_set = []
    wrong_idx = -1
    
    for idx, word in enumerate(words):
        if before != word[0] or word in word_set:
            wrong_idx = idx
            break
        word_set.append(word)
        before = word[-1]
    if wrong_idx == - 1:
        return [0, 0]
    number = wrong_idx % n + 1
    order = (wrong_idx+1) // n if (wrong_idx+1)%n == 0 else (wrong_idx+1)//n + 1
    
    return [number, order]