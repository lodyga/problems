r"""
Binary Decision Tree
                                []
                      /                  \
                    [1]                   []
               /        \              /     \
           [1, 2]       [1]         [2]       []
          /     \          \      /    \         \
    [1,2,2]    [1,2]       [1] [2,2]   [2]        []
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
        nums.sort()
        N = len(nums)
        subset = []
        res = []

        def backtrack(idx):
            if idx == N:
                res.append(subset.copy())
                return

            subset.append(nums[idx])
            backtrack(idx + 1)
            subset.pop()
            
            while (idx + 1 < N and nums[idx] == nums[idx + 1]):
                idx += 1

            backtrack(idx + 1)

        backtrack(0)
        return res


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
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: DFS with backtracking
        Smallest → Largest
        """
        nums.sort()
        res = []
        subset = []

        def backtrack(start):
            res.append(subset.copy())

            for index in range(start, len(nums)):
                if index > start and nums[index] == nums[index - 1]:
                    continue  # Skip duplicates
                subset.append(nums[index])
                backtrack(index + 1)
                subset.pop()

        backtrack(0)
        return res


# print(Solution().subsetsWithDup([1, 2, 2]), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
print(sorted(Solution().subsetsWithDup([0])) == sorted([[], [0]]))
print(sorted(Solution().subsetsWithDup([5, 5])) == sorted([[], [5], [5, 5]]))
print(sorted(Solution().subsetsWithDup([1, 2, 2])) == sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]))
print(sorted(Solution().subsetsWithDup([4, 4, 4, 1, 4])) == sorted([[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]))
