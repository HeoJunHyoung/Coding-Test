def solution(myString):
    
    return ''.join(['l' if myString[i] < 'l' else myString[i] for i in range(0, len(myString))])