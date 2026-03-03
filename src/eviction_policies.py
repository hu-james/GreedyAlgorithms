from collections import deque 

def fifo(k, m):
    cache = set()
    queue = deque() 
    misses = 0 
    for request in m: 
        if request in cache: 
            continue
        else: 
            misses += 1 
            if len(cache) >= k:
                removed = queue.popleft()
                cache.remove(removed)
            cache.add(request)
            queue.append(request)
    return misses 

def lru(k, m):
    misses = 0  
    return misses 

def optff(k, m):
    misses = 0  
    return misses 