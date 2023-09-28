def solution(myString, pat):
    
    last_index = 0
    
    for i in range(0, len(myString)):
        if myString[i:i + len(pat)] == pat:
            last_index = i + len(pat)
    
    return myString[0:last_index]