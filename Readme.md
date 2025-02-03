# Algorithms for Problem Solving

## Problem Representation

### **Exercise 1: Binary Search**
Binary search is a divide-and-conquer algorithm used to find an element in a sorted array. Instead of scanning each element, it divides the array into halves to locate the target efficiently.

#### Example:
- Input: Sorted list = [1, 3, 5, 7, 9, 11], Target = 5
- Output: Index = 2

### **Exercise 2: Graph Traversal (BFS & DFS)**
Graph traversal algorithms help in exploring graphs efficiently. BFS uses a queue for level-wise exploration, whereas DFS uses recursion or a stack to explore as deep as possible before backtracking.

#### Example:
- Input: Graph with nodes {A, B, C, D, E} and edges {(A,B), (A,C), (B,D), (C,E)}
- Output: BFS Order = [A, B, C, D, E], DFS Order = [A, C, E, B, D]

### **Exercise 3: Knapsack Problem**
Given a set of items with weight and value, determine the maximum value that can be obtained within a weight limit.

#### Example:
- Input: Items = [(60, 10), (100, 20), (120, 30)], Max weight = 50
- Output: Max value = 220

### **Exercise 4: Merge Intervals**
Given overlapping intervals, merge them to provide a simplified representation.

#### Example:
- Input: [(1,3), (2,6), (8,10), (15,18)]
- Output: [(1,6), (8,10), (15,18)]

### **Exercise 5: Maximum Subarray Sum (Kadane’s Algorithm)**
Find the contiguous subarray with the maximum sum.

#### Example:
- Input: [-2,1,-3,4,-1,2,1,-5,4]
- Output: 6 (subarray: [4, -1, 2, 1])

---

## Solution and Code

### **Binary Search Implementation**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### **Graph Traversal (BFS & DFS)**
```python
from collections import deque

def bfs(graph, start):
    visited, queue = set(), deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited

def dfs(graph, start, visited=set()):
    if start not in visited:
        visited.add(start)
        for neighbor in graph[start] - visited:
            dfs(graph, neighbor, visited)
    return visited
```

### **0/1 Knapsack Problem**
```python
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w-weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]
```

### **Merging Intervals**
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged
```

### **Kadane’s Algorithm**
```python
def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```

---

## Results

| Algorithm | Input | Output |
|-----------|-------|--------|
| Binary Search | [1, 3, 5, 7, 9], 5 | Index 2 |
| BFS | Graph {A,B,C,D}, Start A | [A, B, C, D] |
| DFS | Graph {A,B,C,D}, Start A | [A, C, B, D] |
| Knapsack | Items [(60,10), (100,20), (120,30)], W=50 | 220 |
| Merge Intervals | [(1,3), (2,6), (8,10)] | [(1,6), (8,10)] |
| Kadane’s Algorithm | [-2,1,-3,4,-1,2,1,-5,4] | 6 |

---

## Conclusion
These advanced algorithms provide efficient solutions to complex problems. Binary search significantly reduces search time compared to linear search. BFS and DFS effectively traverse graphs for connectivity analysis. The Knapsack problem optimizes resource allocation using dynamic programming. Merge intervals simplify scheduling, and Kadane’s algorithm efficiently finds maximum subarray sums.

---

## GitHub Repository
[GitHub Repository Link] (Provide actual link)

