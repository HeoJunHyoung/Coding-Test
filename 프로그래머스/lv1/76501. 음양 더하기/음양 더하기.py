def solution(absolutes, signs):
    
    result = 0
    
    return sum([absolutes[i] if signs[i]==True else -1*absolutes[i] for i in range(0, len(absolutes))])
