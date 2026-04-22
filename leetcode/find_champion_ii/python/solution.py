class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        """
        Time complexity: O(V + E)
        Auxiliary space complexity: O(V)
        Tags:
            DS: array
            A: iteration
        """
        candidates = [0] * n
        res = -1

        for (_, v) in edges:
            candidates[v] += 1

        for (candidate, counter) in enumerate(candidates):
            if counter == 0:
                if res == -1:
                    res = candidate
                else:
                    return -1

        return res


print(Solution().findChampion(3, [[0, 1], [1, 2]]) == 0)
print(Solution().findChampion(4, [[0, 2], [1, 3], [1, 2]]) == -1)
print(Solution().findChampion(3, [[0, 2], [1, 0]]) == 1)
print(Solution().findChampion(1, []) == 0)
print(Solution().findChampion(3, [[0, 1]]) == -1)
print(Solution().findChampion(4, [[0, 1], [2, 0], [2, 1]]) == -1)
