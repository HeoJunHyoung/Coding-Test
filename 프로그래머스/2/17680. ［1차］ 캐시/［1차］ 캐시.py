from collections import deque

def solution(cacheSize, cities):
    
    cache = deque()
    running_time = 0
    cities = [city.upper() for city in cities]
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        if len(cache)+1 <= cacheSize:
            if city not in cache:
                cache.append(city)
                running_time += 5
            else:
                delete_index = cache.index(city)
                cache.append(cache[delete_index])
                del cache[delete_index]
                running_time += 1
        elif len(cache)+1 > cacheSize:
            if city not in cache:
                cache.popleft()
                cache.append(city)
                running_time += 5
            else:
                delete_index = cache.index(city)
                cache.append(cache[delete_index])
                del cache[delete_index]
                running_time += 1
        
    return running_time