class Solution:
    def subarraySum(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash map
        """
        subarray_counter = 0
        cache = {0: 1}
        curent_sum = 0
        
        for number in numbers:
            curent_sum += number
            if curent_sum - target in cache:
                subarray_counter += cache[curent_sum - target]

            cache[curent_sum] = cache.get(curent_sum, 0) + 1

        return subarray_counter


class Solution:
    def subarraySum(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: brute-force
        """
        subarray_counter = 0

        for left in range(len(numbers)):
            current_sum = 0
            for right in range(left, len(numbers)):
                current_sum += numbers[right]
                if current_sum == target:
                    subarray_counter += 1

        return subarray_counter


print(Solution().subarraySum([1, 1, 1], 2) == 2)
print(Solution().subarraySum([1, 2, 3], 3) == 2)
print(Solution().subarraySum([1], 0) == 0)
print(Solution().subarraySum([-1, -1, 1], 0) == 1)
print(Solution().subarraySum([1, -1, 1, 1, 1], 2) == 4)