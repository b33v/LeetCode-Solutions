class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(a: str, b: str) -> bool:
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        def find(parent: List[int], x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent: List[int], x: int, y: int) -> None:
            parent[find(parent, y)] = find(parent, x)

        n = len(strs)
        parent = [i for i in range(n)]
        groups = n

        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]) and find(parent, i) != find(parent, j):
                    union(parent, i, j)
                    groups -= 1

        return groups
