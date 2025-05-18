class Solution:
    def permute(self, numbers: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        """
        permutationList = []

        def dfs(start):
            if start == len(numbers):
                permutationList.append(numbers.copy())
                return

            for index in range(start, len(numbers)):
                numbers[start], numbers[index] = numbers[index], numbers[start]
                dfs(start + 1)
                numbers[start], numbers[index] = numbers[index], numbers[start]
        
        dfs(0)
        return permutationList


print(Solution().permute([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
print(Solution().permute([0, 1]), [[0, 1], [1, 0]])
print(Solution().permute([1]), [[1]])