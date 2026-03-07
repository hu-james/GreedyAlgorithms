# Greedy Algorithms
## Contributors
James Hu (78869080), Priya Khatri (24056337) 

## Repository Overview
This repository contains source code for implementing FIFO, LRU, and OPTFF algorithms and written answers to the questions below. 

## Repository Structure

```
GreedyAlgorithms/
├── src/
│   └── eviction_policies.py - Source code with FIFO, LRU, OPTFF implementations, main, parsing & file IO 
├── tests/ - contains sample test cases 1-3 and the request sequence test for Q2 
└── README.md 
```

## Assumptions 

### Input Format 
Input should be an .in file in tests/ with the format:
```
k m 
r1 r2 r3 ... rm
``` 

k should be >= 1, and m must equal the length of the sequence. 

### Output Format 
Output will be an .out file with the same name as the input file. Its content will be the format: 
```
FIFO: <n_misses>
LRU: <n_misses>
OPTFF: <n_misses>
```


## Code Instructions
First set up Python in your environment. 

Then clone the repository: 
``` 
git clone https://github.com/hu-james/GreedyAlgorithms.git
cd GreedyAlgorithms 
```

To test the code on the 3 provided default test cases in tests/, simply run:

```
python src/eviction_policies.py
``` 

To test the code on your own test cases, move them to the tests/ directory and run: 
```
python src/eviction_policies.py tests/YOUR_TEST.in 
```

## Questions 

### Question 1: Empirical Comparison 

| Input File | k | m | FIFO | LRU | OPTFF | 
| :--- | :---: | :---: | :---: | :---: | :---: |
| test1 | 3 | 70 | 47 | 25 | 25 |
| test2 | 4 | 60 | 50 | 40 | 18 |
| test3 | 5 | 55 | 38 | 30 | 20 |

Yes, OPTFF has the least amount of misses, as seen in our 3 non trivial test outputs. The reason why this is optimal is because it removes the least needed (or farthest needed) item from the cache, reducing cache misses. LRU removes the item that is least recently used, but just because an item was not recently used doesn't mean that it won't get referenced in the future. Because OPTFF checks what requests will be made in the future it is able to greedily avoid cache misses.

LRU performs better than FIFO as seen in our 3 test cases. The reason this occurs is because LRU removes items from the cache that haven't been referenced in a while and keep the most popular items in the cache. Assuming recency bias, items that have been referenced frequently will most likely be referenced again too. So LRU reduces cache misses by focusing on recency when compared to FIFO. 

### Question 2: Bad Sequence for LRU or FIFO 

There does exist a sequence for k = 3 such that OPTFF always has fewer misses than FIFO. One such sequence is (1, 2, 3, 4, 5, 6, 1, 2, 3). In such a case, OPTFF incurs 7 misses, while both FIFO and LRU incur 9 misses (see tests/q2.out). This is because OPTFF is an offline algorithm that's aware of the future sequence and evicts items 3,4, and 5 from the queue because 3 is the farthest next request and 4, 5 are never requested again. Thus, when items like 1 and 2 do not incur misses because they are retained in the cache. Meanwhile, FIFO does not have awareness of future request sequences and ejects items 1, 2, and 3 after 4, 5, and 6 are populated into the cache. Overall, OPTFF incurs fewer misses because it knows about bursts of one-time requests which are evicted by LRU/FIFO and cause misses for items that are needed soon. 


### Question 3: Prove OPTFF is Optimal 

We are trying to prove that the number of misses for OPTFF is no more than (less than or equal to) the number of misses of A where A can be any offline algorithm that knows the full request sequence. 

For all offline algorithms, an item n is only placed in the cache when it is requested if it is not already present. Items are evicted from the cache once the cache limit size has been reached and a new request is made. 

Base case: j = 0, before any requests are made both OPTFF and A have empty caches. 
Assume that for the first j requests, both caches for A and OPTFF are identical. Therefore, the caches for both scenarios are the same until request j + 1. Let the next cache request be i. 

Case 1: If i is already in the cache then no evictions are made for either A or OPTFF, and the cache remains identical. 

Case 2: i is not in the cache. 
Let OPTFF evict item x from the cache and let A evict item y from the cache. If x == y, then even after the eviction the caches for A and OPTFF are the same. 

Otherwise the caches for OPTFF and will differ after request i. Let k be the next request made after i where the caches are now different.
We know that g can not equal x because x was evicted from the cache by OPTFF and if x is the next referenced item, then OPTFF would not have evicted it from the cache, it would have evicted another item. 
If g == y, then offline algorithm A will result in a miss because it evicted item y in the last request. Alternately, OPTFF will not result in a miss because y is still in its cache. This means that for this scenario, the number of misses for A will exceed the number of misses for OPTFF by 1. 
If g is not equal to either x or y then both OPTFF and A will result in a miss, and the number of misses will remain equal. 

So by proof of induction on the base case, the number of misses for OPTFF will always be less than or equal to the number of misses for any offline algorithm A. 