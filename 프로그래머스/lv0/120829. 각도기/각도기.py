def solution(angle):
    
    if angle>0 and angle<=90:
        return 1 if angle<90 else 2
    elif angle>90 and angle<=180:
        return 3 if angle<180 else 4