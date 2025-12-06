r"""
Binary Decision Tree 
                                []
                          /             \
                    [1]                   []
                 /      \              /     \
           [1, 2]       [1]         [2]       []
          /     \          \      /    \         \
  [1,2,3]     [1,2]       [1]  [2,3]  [2]         []
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
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
        nums.sort()

        def backtrack(index: int) -> None:
            if index == len(nums):
                subset_list.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop()
            while (
                index + 1 < len(nums) and
                nums[index] == nums[index + 1]
            ):
                index += 1

            backtrack(index + 1)

        backtrack(0)
        return subset_list


"""
DFS with iteration — Tree Diagram
[]
├── [1]
│   ├── [1, 2]
│   │   └── [1, 2, 2]
└── [2]
    └── [2, 2]
"""


class Solution:
    def subsetsWithDup(self, numbers: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: list
            A: DFS with backtracking
        Smallest → Largest
        """
        numbers.sort()
        subset_list = []
        subset = []

        def backtrack(start):
            subset_list.append(subset.copy())

            for index in range(start, len(numbers)):
                if index > start and numbers[index] == numbers[index - 1]:
                    continue  # Skip duplicates
                subset.append(numbers[index])
                backtrack(index + 1)
                subset.pop()

        backtrack(0)
        return subset_list


print(Solution().subsetsWithDup([0]), [[], [0]])
print(Solution().subsetsWithDup([5, 5]), [[], [5], [5, 5]])
print(Solution().subsetsWithDup([1, 2, 2]), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
print(Solution().subsetsWithDup([4, 4, 4, 1, 4]), [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]])
