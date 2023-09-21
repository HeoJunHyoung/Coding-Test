def dateToday(today):
    year, month, date = map(int, today.split('.'))
    #print(year, month, date)
    return year*12*28+month*28+date

def solution(today, terms, privacies):
    answer = []
    today = dateToday(today)
    termsInfo = dict()
    for term in terms:
        term = term.split()
        termsInfo[term[0]] = int(term[1])*28

    for i in range(len(privacies)):
        date, term = privacies[i].split()
        if dateToday(date)+termsInfo[term] <= today:
                answer.append(i+1)

    return answer

