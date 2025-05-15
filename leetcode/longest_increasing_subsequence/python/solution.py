"""
draft
[10, 9, 2, 5, 3, 7, 101, 18]
[1, 1, 1, 2, 2, max(2,2)+1=3, 4, 1]

brute-force
[2, 8, 4, 5]
                 .
        /               \
        2               .
      /   \           /   \
     8    .          8     .
    / \  / \        / \   / \
   4  . 4   .      4  .  4   .
  /\ /\ /\  /\    /\  /\ /\  /\
  5. 5. 5.  5.    5.  5.  5.  5.
"""


class Solution:
    def lengthOfLIS(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up with cache as list
        """
        # LIS lengths
        cache = [1] * len(numbers)

        for right in range(len(numbers)):
            for left in range(right):
                if numbers[left] < numbers[right]:
                    cache[right] = max(cache[right],
                                       cache[left] + 1)

        return max(cache)


class Solution:
    def lengthOfLIS(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up with cache as hash map
        """
        # LIS lengths
        cache = {}

        for right, number in enumerate(numbers):
            cache[number] = 1

            for left_number in cache.keys():
                if left_number < number:
                    cache[number] = max(cache[number],
                                        cache[left_number] + 1)

        return max(cache.values())


class Solution:
    def lengthOfLIS(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map, mle
        """
        memo = {}

        def dfs(index, prev_index):
            if index == len(numbers):
                return 0
            elif (index, prev_index) in memo:
                return memo[(index, prev_index)]

            # try when current number is skipped
            longest_sub = dfs(index + 1, prev_index)

            # try when current number is greater than previous one
            if (prev_index == -1 or
                    numbers[index] > numbers[prev_index]):
                longest_sub = max(longest_sub, 1 + dfs(index + 1, index))

            memo[(index, prev_index)] = longest_sub
            return longest_sub

        return dfs(0, -1)


class Solution:
    def lengthOfLIS(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, pure recursion, tle, mle, converts to top-down
        """
        def dfs(index, prev_index):
            if index == len(numbers):
                return 0

            # try when current number is greater than previous one
            if (prev_index == -1 or
                    numbers[prev_index] < numbers[index]):
                longest_sub = max(longest_sub, 1 + dfs(index + 1, index))

            # try when current number is skipped
            longest_sub = max(longest_sub, dfs(index + 1, prev_index))

            return longest_sub

        return dfs(0, -1)


class Solution:
    def lengthOfLIS(self, numbers: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, backtracking, tle
        """
        subsequence = []
        self.longest_sub = 0

        def dfs(index):
            if index == len(numbers):
                self.longest_sub = max(self.longest_sub, len(subsequence))
                return

            # check when current number is greater than previous one
            if not subsequence or subsequence[-1] < numbers[index]:
                subsequence.append(numbers[index])
                dfs(index + 1)
                subsequence.pop()

            # check when current number is skipped
            dfs(index + 1)

        dfs(0)
        return self.longest_sub


class Solution:
    def lengthOfLIS(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, function argument, tle
        """
        self.longest_sub = 0

        def dfs(index, subsequence):
            if index == len(numbers):
                self.longest_sub = max(self.longest_sub, len(subsequence))
                return

            # try when current number is greater than previous one
            if not subsequence or subsequence[-1] < numbers[index]:
                dfs(index + 1, subsequence + [numbers[index]])

            # try when current number is skipped
            dfs(index + 1, subsequence)

        dfs(0, [])
        return self.longest_sub


print(Solution().lengthOfLIS([5]) == 1)
print(Solution().lengthOfLIS([5, 6]) == 2)
print(Solution().lengthOfLIS([5, 4]) == 1)
print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4)
print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4)
print(Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1)
print(Solution().lengthOfLIS([4, 10, 4, 3, 8, 9]) == 3)
print(Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6)