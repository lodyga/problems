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
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: DFS with backtracking
        Largest → Smallest
        """
        subset = []
        subset_list = []

        def backtrack(index: int) -> None:
            if index == len(nums):
                subset_list.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop()
            backtrack(index + 1)

        backtrack(0)
        return subset_list


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: DFS with backtracking
        Smallest → Largest
        """
        subset = []
        subset_list = []

        def backtrack(index: int) -> None:
            if index == len(nums):
                subset_list.append(subset.copy())
                return

            backtrack(index + 1)
            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop()

        backtrack(0)
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
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: DFS with backtracking
        Smallest → Largest
        """
        subset_list = []
        subset = []

        def backtrack(start):
            subset_list.append(subset.copy())  # append early
            for index in range(start, len(nums)):
                subset.append(nums[index])
                backtrack(index + 1)
                subset.pop()

        backtrack(0)
        return subset_list


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: DFS with backtracking
        Largest → Smallest
        """
        subset_list = []
        subset = []

        def backtrack(start):
            for index in range(start, len(nums)):
                subset.append(nums[index])
                backtrack(index + 1)
                subset.pop()
            subset_list.append(subset.copy())  # append after recursion

        backtrack(0)
        return subset_list


print(Solution().subsets([0]))
print(Solution().subsets([1, 2, 3]))
print(Solution().subsets([1, 2]))

print(sorted(Solution().subsets([0])) == [[], [0]])
print(sorted(Solution().subsets([1, 2])) == [[], [1], [1, 2], [2]])
print(sorted(Solution().subsets([1, 2, 3])) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
