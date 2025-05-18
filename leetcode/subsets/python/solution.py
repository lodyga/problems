r"""
Binary Decision Tree 
                                []
                          /             \
                    [1]                   []
                 /      \              /     \
           [1, 2]       [1]         [2]       []
          /     \      /   \      /    \     /   \
  [1,2,3]   [1,2]  [1,3]  [1]  [2,3]  [2]  [3]   []
"""


class Solution:
    def subsets(self, numbers: list[int]) -> list[list[int | None]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        Largest → Smallest
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


class Solution:
    def subsets(self, numbers: list[int]) -> list[list[int | None]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        Smallest → Largest
        """
        subset = []
        subset_list = []

        def dfs(index: int) -> None:
            if index == len(numbers):
                subset_list.append(subset.copy())
                return

            dfs(index + 1)
            subset.append(numbers[index])
            dfs(index + 1)
            subset.pop()

        dfs(0)
        return subset_list


"""
DFS with iteration — Tree Diagram
[]
├── [1]
│   ├── [1, 2]
│   │   └── [1, 2, 3]
│   └── [1, 3]
├── [2]
│   └── [2, 3]
└── [3]
"""

class Solution:
    def subsets(self, numbers: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: Iterative DFS with Backtracking
        Smallest → Largest
        """
        subset_list = []
        subset = []

        def dfs(start):
            subset_list.append(subset.copy())  # append early
            for index in range(start, len(numbers)):
                subset.append(numbers[index])
                dfs(index + 1)
                subset.pop()

        dfs(0)
        return subset_list


class Solution:
    def subsets(self, numbers: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: Iterative DFS with Backtracking
        Largest → Smallest
        """
        subset_list = []
        subset = []

        def dfs(start):
            for index in range(start, len(numbers)):
                subset.append(numbers[index])
                dfs(index + 1)
                subset.pop()
            subset_list.append(subset.copy())  # append after recursion

        dfs(0)
        return subset_list


print(Solution().subsets([0]))
print(Solution().subsets([1, 2, 3]))
print(Solution().subsets([1, 2]))

print(sorted(Solution().subsets([0])) == [[], [0]])
print(sorted(Solution().subsets([1, 2])) == [[], [1], [1, 2], [2]])
print(sorted(Solution().subsets([1, 2, 3])) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])