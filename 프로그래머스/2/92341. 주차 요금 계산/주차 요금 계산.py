import math

def splitInfo(record, parking):
    time, car_num, state = record.split(' ')
    hour, minute = time.split(':')
    minutes = int(hour) * 60 + int(minute)
    if car_num not in parking:
        parking[car_num] = ['OUT', 0, 0]
    return parking, minutes, car_num, state

def solution(fees, records):
    
    parking = dict()
    result = []
    
    for record in records:
        parking, time, car_num, state = splitInfo(record, parking)
        
        if parking[car_num][0] == 'IN':
            parking[car_num][2] += time - parking[car_num][1]
            parking[car_num][1] = 0
            parking[car_num][0] = 'OUT'
            
        elif parking[car_num][0] == 'OUT':
            parking[car_num][1] = time
            parking[car_num][0] = 'IN'
    
    for key, value in parking.items():
        if parking[key][0] == 'IN':
            parking[key][2] += (23*60+59) - parking[key][1]
    
    parking_list = sorted(parking)
    for car in parking_list:
        total_money = 0
        if parking[car][2] > fees[0]:
            total_money = fees[1] + math.ceil(((parking[car][2] - fees[0]) / fees[2])) * fees[3]
        else:
            total_money = fees[1]
        result.append(total_money)
    
    return result
    
    