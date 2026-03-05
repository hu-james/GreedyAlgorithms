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

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def parse(filename):
    with open(filename, 'r') as f:
        k, m = map(int, f.readline().split())
        requests = list(map(int, f.readline().split()))

    return k, requests

def lru(filename):
    '''
    in order to keep track of the cached items in the list I will use a hashmap and doubly linked list
    if there is no hit and the queue is too big, remove the head of the linked list and add to the tail
    otherwise check if there is a hit using the hashmap and then remove the linked list node from its position and put it at the end to indicate it was just used
    the hashmap will have key = element value = pointer to the linked list node 
    '''
    k, requests = parse(filename)
    miss = 0
    cache = {}
    # head = LRU and tail = MRU (most recently used)
    head, tail = ListNode(0), ListNode(0)
    head.next = tail
    tail.prev = head

    for element in requests:
        #check if element is already in cache
        if element in cache:
            #remove the element from where it current is
            node = cache[element]
            prev_element, next_element = node.prev, node.next
            next_element.prev = prev_element
            prev_element.next = next_element
            #add the element to the end of linked list
            mru = tail.prev
            mru.next = node
            node.prev = mru
            node.next = tail
            tail.prev = node
        
        else:
            miss += 1
            #we need to add the element to the cache
            if len(cache) >= k:
                #if the cache has reached max length remove lru
                lru = head.next.value
                del cache[lru]
                new_lru = head.next.next
                head.next = new_lru
                new_lru.prev = head
                
            #add element to both cache and end of linked list
            node = ListNode(element)
            cache[element] = node
            mru = tail.prev
            mru.next = node
            node.prev = mru
            node.next = tail
            tail.prev = node

    return miss

def optff(k, m):
    misses = 0  
    return misses 