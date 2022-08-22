def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5*len(cities)
    
    cities_low = list(map(lambda x : x.lower(), cities))
    cache = [cities_low[0]]
    time = 5
    
    for i in range(1, len(cities_low)):
        if cities_low[i] in cache:
            time += 1
            cache.pop(cache.index(cities_low[i]))
        else:
            time += 5
            if len(cache) == cacheSize:
                cache.pop(0)
                
        cache.append(cities_low[i])
        
            
    return time