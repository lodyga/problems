class Solution:
    def maxTurbulenceSize(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        num_iterator = iter(nums)
        prev = next(num_iterator)
        # 1: increasing, 0: decreating, -1: donno
        is_increasing = -1
        size = 1
        max_size = 1

        for num in num_iterator:
            if (
                prev < num and
                is_increasing != 1
            ):
                size += 1
                is_increasing = 1

            elif (
                prev > num and
                is_increasing != 0
            ):
                size += 1
                is_increasing = 0

            else:
                if prev < num:
                    size = 2
                    is_increasing = 1
                elif prev > num:
                    size = 2
                    is_increasing = 0
                else:
                    size = 1
                    is_increasing = -1

            prev = num
            max_size = max(max_size, size)

        return max_size


print(Solution().maxTurbulenceSize([3, 8, 4]) == 3)
print(Solution().maxTurbulenceSize([8, 3, 9]) == 3)
print(Solution().maxTurbulenceSize([1, 3, 8, 4]) == 3)
print(Solution().maxTurbulenceSize([9, 8, 3, 9]) == 3)
print(Solution().maxTurbulenceSize([3, 3]) == 1)
print(Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5)
print(Solution().maxTurbulenceSize([4, 8, 12, 16]) == 2)
print(Solution().maxTurbulenceSize([100]) == 1)
