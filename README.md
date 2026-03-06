# Greedy Algorithms
## Contributors
James Hu (78869080), Priya Khatri (24056337) 

## Repository Overview
This repository contains source code for implementing FIFO, LRU, and OPTFF algorithms and written answers to the questions below. 

## Questions 

### Question 1: Empirical Comparison 

Yes, OPTFF has the least amount of misses, as seen in our 3 non trivial test outputs. The reason why this is optimal is because it removes the least needed (or farthest needed) item from the cache, reducing cache misses. LRU removes the item that is least recently used, but just because an item was not recently used doesn't mean that it won't get referenced in the future. Because OPTFF checks what requests will be made in the future it is able to greedily avoid cache misses.

LRU performs better than FIFO as seen in our 3 test cases. The reason this occurs is because LRU removes items from the cache that haven't been referenced in a while and keep the most popular items in the cache. Assuming recency bias, items that have been referenced frequently will most likely be referenced again too. So LRU reduces cache misses by focusing on recency when compared to FIFO. 

### Question 2: Bad Sequence for LRU or FIFO 

There does exist a sequence for k = 3 such that OPTFF always has fewer misses than FIFO. One such sequence is (1, 2, 3, 4, 5, 6, 1, 2, 3). In such a case, OPTFF incurs 7 misses, while both FIFO and LRU incur 9 misses (see tests/.out). This is because OPTFF is an offline algorithm that's aware of the future sequence and evicts items 3,4, and 5 from the queue because 3 is the farthest next request and 4, 5 are never requested again. Thus, when items like 1 and 2 do not incur misses because they are retained in the cache. Meanwhile, FIFO does not have awareness of future request sequences and ejects items 1, 2, and 3 after 4, 5, and 6 are populated into the cache. Overall, OPTFF incurs fewer misses because it knows about bursts of one-time requests which are evicted by LRU/FIFO and cause misses for items that are needed soon. 


### Question 3: Prove OPTFF is Optimal 
