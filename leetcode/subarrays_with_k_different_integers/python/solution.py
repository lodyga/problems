"""
draft
[1, 2, 1, 2, 3], 2
[1,2],
([1,2,1], [2,1]),
([1,2,1,2], [2,1,2], [1,2]),
[2,3]

[1, 2, 1, 3, 4], 3
[1,2,1,3], [2,1,3],
[1,3,4]
"""


class Solution:
    def subarraysWithKDistinct(self, numbers: list[int], unique_number_counter: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: sliding window
        """
        window = {}  # {number: frequency}
        left = 0
        middle = 0
        subarray_counter = 0

        for number in numbers:
            window[number] = window.get(number, 0) + 1
            
            while len(window) > unique_number_counter:
                middle_number = numbers[middle]
                window[middle_number] -= 1
                
                if window[middle_number] == 0:
                    del window[middle_number]
                
                middle += 1
                left = middle

            # if there is more than one copy of middle number
            # than separate middle from left and move if right
            # while there's at least one copy of each unique number
            middle_number = numbers[middle]
            while window[middle_number] > 1:
                window[middle_number] -= 1
                middle += 1
                middle_number = numbers[middle]

            if len(window) == unique_number_counter:
                subarray_counter += middle - left + 1
        
        return subarray_counter


print(Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2) == 7)
print(Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3) == 3)


# O(n2), O(n)
# brute force
class Solution:
    def subarraysWithKDistinct(self, numbers: list[int], k: int) -> int:
        subarray_counter = 0
        
        for i in range(len(numbers)):
            counter = {}
            
            for j in range(i, len(numbers)):
                counter[numbers[j]] = counter.get(numbers[j], 0) + 1
                if len(counter) == k:
                    subarray_counter += 1
        
        return subarray_counter