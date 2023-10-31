def solution(record):
    
    records = [info.split(' ') for info in record]
    id_nickname = dict()
    before = []
    after = []
    
    for record in records:
        if record[0] == 'Enter':
            id_nickname[record[1]] = record[2]
            before.append([record[1], '님이 들어왔습니다.'])
        elif record[0] == 'Leave':
            before.append([record[1], '님이 나갔습니다.'])
        elif record[0] == 'Change':
            id_nickname[record[1]] = record[2]
    
   # print(before)
    #print(id_nickname)
    
    for user_id, string in before:
        after.append(id_nickname[user_id] + string)
    
    return after