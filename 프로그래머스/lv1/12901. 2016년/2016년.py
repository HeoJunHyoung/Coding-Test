def solution(a, b):
    answer = ''
    weekList = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    monthList = list(range(1, 13))
    month_day = dict(zip(monthList, ['31','29','31','30','31','30','31','31','30','31','30','31']))
    
    total_day = 0
    
    for i in range(1, a):
        total_day += int(month_day[i])
    total_day += b
    
    result = total_day % 7
    return weekList[result-1]