def solution(s):
    
    word_num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for index, value in enumerate(word_num):
        s = s.replace(value, str(index))
    return int(s)