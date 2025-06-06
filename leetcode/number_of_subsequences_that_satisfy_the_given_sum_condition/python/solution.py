class Solution:
    def numSubseq(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: two pointers
        """
        numbers.sort()
        mod = 10 ** 9 + 7
        subsequence_counter = 0
        right = len(numbers) - 1

        for left, left_number in enumerate(numbers):
            while (left <= right and 
                   left_number + numbers[right] > target):
                right -= 1
            
            if left <= right:
                subsequence_counter += pow(2, right - left, mod)
                subsequence_counter %= mod
            
            if left == right:
                break

        return subsequence_counter


class Solution:
    def numSubseq(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: binary search
        """
        numbers.sort()
        mod = 10 ** 9 + 7
        subsequence_counter = 0

        for index in range(len(numbers)):
            if numbers[index] * 2 > target:
                break
            
            left = index
            right = len(numbers) - 1

            while left <= right:
                middle = (left + right) // 2

                if (numbers[index] + numbers[middle]) <= target:
                    left = middle + 1
                else:
                    right = middle - 1
            
            subsequence_counter += pow(2, right - index, mod)
            subsequence_counter %= mod

        return subsequence_counter


print(Solution().numSubseq([3, 5, 6, 7], 9) == 4)
print(Solution().numSubseq([3, 3, 6, 8], 10) == 6)
print(Solution().numSubseq([2, 3, 3, 4, 6, 7], 12) == 61)
print(Solution().numSubseq([7, 10, 7, 3, 7, 5, 4], 12) == 56)
print(Solution().numSubseq([14, 4, 6, 6, 20, 8, 5, 6, 8, 12, 6, 10, 14, 9, 17, 16, 9, 7, 14, 11, 14, 15, 13, 11, 10, 18, 13, 17, 17, 14, 17, 7, 9, 5, 10, 13, 8, 5, 18, 20, 7, 5, 5, 15, 19, 14], 22) == 272187084)
print(Solution().numSubseq([9, 25, 9, 28, 24, 12, 17, 8, 28, 7, 21, 25, 10, 2, 16, 19, 12, 13, 15, 28, 14, 12, 24, 9, 6, 7, 2, 15, 19, 13, 30, 30, 23, 19, 11, 3, 17, 2, 14, 20, 22, 30, 12, 1, 11, 2, 2, 20, 20, 27, 15, 9, 10, 4, 12, 30, 13, 5, 2, 11, 29, 5, 3, 13, 22, 5, 16, 19, 7, 19, 11, 16, 11, 25, 29, 21, 29, 3, 2, 9, 20, 15, 9], 32) == 91931447)


class Solution:
    def numSubseq(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: two pointers
        """
        numbers.sort()
        mod = 10 ** 9 + 7
        subsequence_counter = 0

        for left, left_number in enumerate(numbers):
            if left_number * 2 > target:
                break
            
            right = left
            while (right < len(numbers) and 
                   left_number + numbers[right] <= target):
                right += 1
            
            subsequence_counter += pow(2, right - left - 1, mod)
            subsequence_counter %= mod

        return subsequence_counter


# O(n2^n), O(n)
# backtracking
# slow
class Solution:
    def __init__(self):
        self.counter = 0

    def numSubseq(self, numbers: list[int], target: int) -> int:
        numbers.sort()
        subsequence = []

        def dfs(index):
            if index == len(numbers):
                if (subsequence and 
                        subsequence[0] + subsequence[-1] <= target):
                    self.counter += 1
                return
            
            subsequence.append(numbers[index])
            dfs(index + 1)
            subsequence.pop()
            dfs(index + 1)

        dfs(0)
        return self.counter % (10 ** 9 + 7)


# O(n2^n), O(n)
# backtracking
# slow
class Solution:
    def numSubseq(self, numbers: list[int], target: int) -> int:
        numbers.sort()
        subsequence = []

        def dfs(index, counter):
            if index == len(numbers):
                if (subsequence and 
                        subsequence[0] + subsequence[-1] <= target):
                    return 1
                else:
                    return 0
            
            subsequence.append(numbers[index])
            left = dfs(index + 1, counter)
            subsequence.pop()
            right = dfs(index + 1, counter)
            return (left + right) % (10 ** 9 + 7)

        return dfs(0, 0)
