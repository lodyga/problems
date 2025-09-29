class Solution:
    def maxSumMinProduct(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: brute-force, tle
        """
        mod = 10 ** 9 + 7
        max_min_product = numbers[0]

        for left in range(len(numbers)):
            min_number = numbers[left]
            subarray_sum = 0
            for right in range(left, len(numbers)):
                min_number = min(min_number, numbers[right])
                subarray_sum += numbers[right]
                max_min_product = max(max_min_product, 
                                      min_number * subarray_sum % mod)
        
        return max_min_product


print(Solution().maxSumMinProduct([1]), 1)  # [1] * 1
print(Solution().maxSumMinProduct([1, 2]), 4)  # [2] * 2
print(Solution().maxSumMinProduct([1, 2, 3]), 10)  # [2, 3] * 2
print(Solution().maxSumMinProduct([1, 2, 3, 2]), 14)  # [2, 3, 2] * 2
print(Solution().maxSumMinProduct([2, 3, 3, 1, 2]), 18)  # [3, 3] * 3
print(Solution().maxSumMinProduct([3, 1, 5, 6, 4, 2]), 60)  # [5, 6, 4] * 4