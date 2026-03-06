# Greedy Algorithms
## Contributors
James Hu (78869080), Priya Khatri (24056337) 

## Repository Overview
This repository contains source code for implementing FIFO, LRU, and OPTFF algorithms and written answers to the questions below. 

## Questions 

### Question 1: Empirical Comparison 

Yes, OPTFF has the least amount of misses, as seen in our 3 non trivial test outputs. The raeson why this is optimal is because it removes the least needed (or farthest needed) item from the cache, reducing cache misses. LRU removes the item that is least recently used, but just because an item was not recently used doesn't mean that it won't get referenced in the future. Because OPTFF checks what requests will be made in the future it is able to greedily avoid cache misses.

LRU performs better than FIFO as seen in our 3 test cases. The reason this occurs is because LRU removes items from the cache that haven't been referenced in a while and keep the most popular items in the cache. Assuming recency bias, items that have been referenced frequently will most likely be referenced again too. So LRU reduces cache misses by focusing on recency when compared to FIFO. 

### Question 2: Bad Sequence for LRU or FIFO 

### Question 3: Prove OPTFF is Optimal 
