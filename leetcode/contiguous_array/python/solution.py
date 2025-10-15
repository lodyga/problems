class Solution:
    def findMaxLength(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: prefix sum
        """
        prefixes = {}  # ones over zeros surplus: numbers index
        zeros = 0
        ones = 0
        max_len = 0

        for index, number in enumerate(numbers):
            if number:
                ones += 1
            else:
                zeros += 1
            
            diff = ones - zeros
            if diff not in prefixes:
                prefixes[diff] = index

            if ones == zeros:
                max_len = ones + zeros
            else:
                max_len = max(max_len, index - prefixes[diff])
        
        return max_len


class Solution2:
    def findMaxLength(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        failed attempt, desn't work for the large test case and O(n2)
        """
        # memo = {}
        def dfs(index, zeros, ones):
            if index == len(numbers):
                return zeros + ones if zeros == ones else 0
            # elif zeros == ones and (index, zeros) in memo:
            #     return memo[(index, zeros)]

            number = numbers[index]

            # take
            take = dfs(index + 1, zeros + (number == 0), ones + (number == 1))
            # start
            start = dfs(index + 1, 0, 0)
            # end
            end = zeros + ones if zeros == ones else 0

            # memo[(index, zeros)] = max(take, start, end)
            # return memo[(index, zeros)]
            return max(take, start, end)

        return dfs(0, 0, 0)


print(Solution().findMaxLength([0, 1]) == 2)
print(Solution().findMaxLength([0, 1, 0]) == 2)
print(Solution().findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]) == 6)
print(Solution().findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0, 0]) == 10)
print(Solution().findMaxLength([0, 1, 1]) == 2)
print(Solution().findMaxLength([1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1]) == 94)
print(Solution().findMaxLength([1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1]) == 94)