class Solution:
    def subsets(self, numbers: list[int]) -> list[list[int | None]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        """
        subset = []
        subset_list = []

        def dfs(index: int) -> None:
            if index == len(numbers):
                subset_list.append(subset.copy())
                return

            subset.append(numbers[index])
            dfs(index + 1)
            subset.pop()
            dfs(index + 1)

        dfs(0)
        return subset_list


print(sorted(Solution().subsets([0])) == [[], [0]])
print(sorted(Solution().subsets([1, 2])) == [[], [1], [1, 2], [2]])
print(sorted(Solution().subsets([1, 2, 3])) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])