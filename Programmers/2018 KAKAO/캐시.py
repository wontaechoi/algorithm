def rearrange(cache, index):
    new_cache = []
    for i, c in enumerate(cache):
        if i != index:
            new_cache.append(c)
    new_cache.append(cache[index])
    return new_cache

def solution(cacheSize, cities):
    cache = []
    answer = 0
    for city in cities:
        city = city.lower()
        if city not in cache:
            answer += 5
            if cacheSize != 0:
                if len(cache) == cacheSize:
                    cache = cache[1:]
                cache.append(city)
        else:
            index = cache.index(city)
            cache = rearrange(cache, index)
            answer += 1
    return answer
