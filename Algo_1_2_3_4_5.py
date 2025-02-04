from collections import deque

class AlgorithmSolver:
    """Classe regroupant plusieurs algorithmes de résolution de problèmes."""

    @staticmethod
    def binary_search(arr, target):
        """La Recherche binaire dans un tableau trié."""
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
#EXO1
    @staticmethod
    def bfs(graph, start):
        """Ici on fait le parcours en largeur (BFS) d'un graphe."""
        visited, queue = set(), deque([start])
        order = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                queue.extend(graph[node] - visited)
        return order
#EXO2
    @staticmethod
    def dfs(graph, start, visited=None):
        """Cet algo parcours en profondeur (DFS) d'un graphe."""
        if visited is None:
            visited = set()
        visited.add(start)
        order = [start]
        for neighbor in graph[start] - visited:
            order.extend(AlgorithmSolver.dfs(graph, neighbor, visited))
        return order
#EXO3
    @staticmethod
    def knapsack(values, weights, capacity):
        """Cet algo fair la résolution du problème du sac à dos (0/1 Knapsack)."""
        n = len(values)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for w in range(capacity + 1):
                if weights[i-1] <= w:
                    dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w-weights[i-1]])
                else:
                    dp[i][w] = dp[i-1][w]
        return dp[n][capacity]
#EXO4
    @staticmethod
    def merge_intervals(intervals):
        """CET ALGO Fusionne des intervalles qui se chevauchent."""
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))
        return merged
#EXO5
    @staticmethod
    def max_subarray_sum(arr):
        """Algo de Kadane pour la somme maximale d'un sous-tableau."""
        max_sum = current_sum = arr[0]
        for num in arr[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
