class Solution:
    def maxTurbulenceSize(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        prev_number = numbers[0]
        turb_size = 1
        max_turb_size = 1
        # in the next loop assume that current number (as prev number) would be less than the current number
        # if not then sequence is not turbulent
        assume_next_less = True
        # in the next loop assume that current number (as prev number) would be greater than the current number
        # if not then sequence is not turbulent
        assume_next_greater = True

        for number in numbers[1:]:
            if prev_number < number:
                turb_size = turb_size + 1 if assume_next_greater else 2
                assume_next_less = True
                assume_next_greater = False
            elif prev_number > number:
                turb_size = turb_size + 1 if assume_next_less else 2
                assume_next_greater = True
                assume_next_less = False
            else:
                turb_size = 1
                assume_next_greater = True
                assume_next_less = True

            prev_number = number
            max_turb_size = max(max_turb_size, turb_size)
        
        return max_turb_size


print(Solution().maxTurbulenceSize([3, 8, 4]), 3)
print(Solution().maxTurbulenceSize([8, 3, 9]), 3)
print(Solution().maxTurbulenceSize([1, 3, 8, 4]), 3)
print(Solution().maxTurbulenceSize([9, 8, 3, 9]), 3)
print(Solution().maxTurbulenceSize([3, 3]), 1)
print(Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]), 5)
print(Solution().maxTurbulenceSize([4, 8, 12, 16]), 2)
print(Solution().maxTurbulenceSize([100]), 1)