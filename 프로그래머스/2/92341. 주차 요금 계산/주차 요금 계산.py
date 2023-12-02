def convertHourToMin(time):
    hours, minutes = list(map(int, time.split(':')))
    return hours * 60 + minutes

def solution(fees, records):
    
    car_dict = dict()
    total_price = []
    
    for record in records:
        time, car_num, state = record.split(' ')
        time = convertHourToMin(time)
        if car_num not in car_dict:
            car_dict[car_num] = [time, 1, 0]
        else:
            if car_dict[car_num][1] == 1:
                car_dict[car_num] = [0, 0, car_dict[car_num][2] + time - car_dict[car_num][0]]
            else:
                car_dict[car_num] = [time, 1, car_dict[car_num][2]]
        
    for key, value in car_dict.items():
        if value[1] == 1:
            car_dict[key] = [0, 0, value[2] + convertHourToMin("23:59") - car_dict[key][0]]
    
    car_dict = sorted(car_dict.items(), key=lambda x : x[0])
    
    
    for idx, value in enumerate(car_dict):
        if value[1][2] > fees[0]:
            if (value[1][2]-fees[0]) % fees[2] == 0:
                total_price.append(fees[1] + ((value[1][2]-fees[0])/fees[2] * fees[3]))
            else:
                total_price.append(fees[1] + (((value[1][2]-fees[0])//fees[2]+1) * fees[3]))
        else:
            total_price.append(fees[1])
    return total_price
    
    