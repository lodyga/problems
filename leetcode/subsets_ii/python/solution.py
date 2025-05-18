r"""
Binary Decision Tree 
                                []
                          /             \
                    [1]                   []
                 /      \              /     \
           [1, 2]       [1]         [2]       []
          /     \          \      /    \         \
  [1,2,3]   [1,2]         [1]  [2,3]  [2]         []
"""


class Solution:
    def subsetsWithDup(self, numbers: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        Largest → Smallest
        """
        numbers.sort()
        subset = []
        subset_list = []  # 5,5 5, 5, 0

        def dfs(index):
            if index == len(numbers):
                subset_list.append(subset.copy())
                return

            subset.append(numbers[index])
            dfs(index + 1) # 1,0[5], 2,1[5,5] 5,1[5]
            subset.pop()
            # Skip over duplicate elements to avoid generating duplicate subsets
            # If the next number at the `index + 1` is the same as 
            # the number at the current `index` (that was popped) skip it.
            while (index + 1 < len(numbers) and
                    numbers[index] == numbers[index + 1]):
                index += 1
            dfs(index + 1)  # 3,1[5] 4,0[] 6,1[]
            return
        
        dfs(0)
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
        Tags: Iterative DFS with Backtracking
        Smallest → Largest
        """
        numbers.sort()
        subset_list = []
        subset = []

        def dfs(start):
            subset_list.append(subset.copy())
            
            for index in range(start, len(numbers)):
                if index > start and numbers[index] == numbers[index - 1]:
                    continue  # Skip duplicates
                subset.append(numbers[index])
                dfs(index + 1)
                subset.pop()

        dfs(0)
        return subset_list


print(Solution().subsetsWithDup([0]), [[], [0]])
print(Solution().subsetsWithDup([5, 5]), [[], [5], [5, 5]])
print(Solution().subsetsWithDup([1, 2, 2]), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
print(Solution().subsetsWithDup([4, 4, 4, 1, 4]), [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]])