def solution(cacheSize, cities):
    
    time = 0
    memory = []
    cities = [city.lower() for city in cities]
    
    if cacheSize==0:
        return len(cities)*5
    else:
        for city in cities:
            if len(memory) < cacheSize:
                if city not in memory:
                    memory.append(city)
                    time += 5

                else:
                    recall = memory.pop(memory.index(city))
                    memory.append(recall)
                    time += 1

            else:
                if city not in memory:
                    memory.pop(0)
                    memory.append(city)
                    time += 5

                else:
                    recall = memory.pop(memory.index(city))
                    memory.append(recall)
                    time += 1
                
    return time