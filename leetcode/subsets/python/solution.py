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
        N = len(nums)
        subset = []
        res = []

        def backtrack(idx: int) -> None:
            if idx == N:
                res.append(subset.copy())
                return

            subset.append(nums[idx])
            backtrack(idx + 1)
            subset.pop()
            backtrack(idx + 1)

        backtrack(0)    
        return res


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
        N = len(nums)
        subset = []
        res = []

        def backtrack(idx: int) -> None:
            if idx == N:
                res.append(subset.copy())
                return

            backtrack(idx + 1)
            subset.append(nums[idx])
            backtrack(idx + 1)
            subset.pop()

        backtrack(0)    
        return res


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
        res = []
        subset = []

        def backtrack(start):
            res.append(subset.copy())  # append early

            for idx in range(start, len(nums)):
                subset.append(nums[idx])
                backtrack(idx + 1)
                subset.pop()

        backtrack(0)
        return res


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
        res = []
        subset = []

        def backtrack(start):
            for idx in range(start, len(nums)):
                subset.append(nums[idx])
                backtrack(idx + 1)
                subset.pop()
            
            res.append(subset.copy())  # append after recursion

        backtrack(0)
        return res


# print(Solution().subsets([0]))
# print(Solution().subsets([1, 2, 3]))
# print(Solution().subsets([1, 2]))
print(sorted(Solution().subsets([0])) == sorted([[], [0]]))
print(sorted(Solution().subsets([1, 2])) == sorted([[], [1], [1, 2], [2]]))
print(sorted(Solution().subsets([1, 2, 3])) == sorted([[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]))
