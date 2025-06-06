class Solution:
    def numSubarrayProductLessThanK(self, numbers: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        left = 0
        window_product = 1
        subarray_counter = 0

        for right in range(len(numbers)):
            window_product *= numbers[right]

            while (left <= right and window_product >= k):
                window_product //= numbers[left]
                left += 1

            subarray_counter += right - left + 1

        return subarray_counter


print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100), 8)
print(Solution().numSubarrayProductLessThanK([1, 2, 3], 0), 0)
print(Solution().numSubarrayProductLessThanK([1, 1, 1], 1), 0)
print(Solution().numSubarrayProductLessThanK([57, 44, 92, 28, 66, 60, 37, 33, 52, 38, 29, 76, 8, 75, 22], 18), 1)


# O(n3), O(1)
# brute force
class Solution:
    def numSubarrayProductLessThanK(self, numbers: list[int], k: int) -> int:
        counter = 0
        
        for left in range(len(numbers)):
            for right in range(left, len(numbers)):
                window = 1
        
                for number in numbers[left: right + 1]:
                    window *= number
                
                if window < k:
                    counter += 1
        
        return counter


# O(n2), O(1)
# brute force
class Solution:
    def numSubarrayProductLessThanK(self, numbers: list[int], k: int) -> int:
        counter = 0
        
        for left in range(len(numbers)):
            window = 1
      
            for right in range(left, len(numbers)):
                window *= numbers[right]
                
                if window < k:
                    counter += 1
        
        return counter
