class Solution:
    def numOfSubarrays(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: prefix sum
        """
        MOD = 10**9 + 7
        subarray_counter = 0
        odd_counter = 0
        even_counter = 0

        prefix_sum = 0
        for number in numbers:
            prefix_sum += number
            
            if prefix_sum % 2:
                subarray_counter += 1 + even_counter
                odd_counter += 1
            else:
                subarray_counter += odd_counter
                even_counter += 1
            subarray_counter %= MOD

        return subarray_counter


class Solution:
    def numOfSubarrays(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: brute-force
        """
        MOD = 10**9 + 7
        counter = 0
        
        for index in range(len(numbers)):
            total = 0

            for right in range(index, len(numbers)):
                total += numbers[right]
                
                if total % 2:
                    if counter == MOD:
                        counter = 1
                    else:
                        counter += 1
        
        return counter


print(Solution().numOfSubarrays([3]) == 1)
print(Solution().numOfSubarrays([1, 3, 5]) == 4)
print(Solution().numOfSubarrays([2, 4, 6]) == 0)
print(Solution().numOfSubarrays([1, 2, 3, 4]) == 6)
print(Solution().numOfSubarrays([1, 2, 3, 4, 5, 6, 7]) == 16)