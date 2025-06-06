class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
            O(n2^numbers)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        """
        combination = []
        combination_list = []
        numbers = range(1, n + 1)

        def dfs(index):
            if len(combination) == k:
                combination_list.append(combination.copy())
                return
            if index == n:
                return

            combination.append(numbers[index])
            dfs(index + 1)
            combination.pop()
            dfs(index + 1)

        dfs(0)
        return combination_list


print(Solution().combine(1, 1), [[1]])
print(Solution().combine(2, 2), [[1, 2]])
print(Solution().combine(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])