def solution(id_list, report, k):
    
    report_list = []
    id_report = dict(zip(id_list, [0]*len(id_list)))
    id_num = {id: [] for id in id_list}
    result = dict(zip(id_list, [0]*len(id_list)))
    
    for i in range(len(report)):
        my_id, report_id = report[i].split(' ')
        if report_id in id_num[my_id] :
            continue
        id_num[my_id].extend([report_id])
        id_report[report_id] += 1
        

    reported_list = [key for key, value in id_report.items() if value >= k]
    #print(reported_list)
    for name in reported_list:
        for key, value in id_num.items():
            if name in value:
                result[key] += 1
    
    return [value for value in result.values()]
    
    
    
    
    
    
    
    
    
    