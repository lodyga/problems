class Solution:
    def maxTurbulenceSize(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        prev_num = nums[0]
        sub_size = 1
        res = 1
        # increasing: 1, decreasing: 0: donno: -1
        is_increasing = -1

        for num in nums:
            if prev_num == num:
                is_increasing = -1
                sub_size = 1
            elif prev_num > num and is_increasing != 1:
                sub_size += 1
                is_increasing = 1
                res = max(res, sub_size)
            elif prev_num < num and is_increasing != 0:
                sub_size += 1
                is_increasing = 0
                res = max(res, sub_size)
            # New monotonic pair.
            else:
                sub_size = 2

            prev_num = num

        return res


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
        # increasing: 1, decreasing: 0: donno: -1
        is_increasing = -1
        size = 1
        res = 1

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
            res = max(res, size)

        return res


print(Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5)
print(Solution().maxTurbulenceSize([4, 8, 12, 16]) == 2)
print(Solution().maxTurbulenceSize([100]) == 1)
print(Solution().maxTurbulenceSize([0, 1, 1, 0, 1, 0, 1, 1, 0, 0]) == 5)
print(Solution().maxTurbulenceSize([2, 0, 2, 4, 2, 5, 0, 1, 2, 3]) == 6)
print(Solution().maxTurbulenceSize([3, 8, 4]) == 3)
print(Solution().maxTurbulenceSize([8, 3, 9]) == 3)
print(Solution().maxTurbulenceSize([1, 3, 8, 4]) == 3)
print(Solution().maxTurbulenceSize([9, 8, 3, 9]) == 3)
print(Solution().maxTurbulenceSize([3, 3]) == 1)
