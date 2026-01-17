class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: two pointers
        """
        nums.sort()
        res = nums.copy()

        mid = len(nums) >> 1
        index = 0

        if len(nums) % 2:
            res[0] = nums[mid]
            left = mid - 1
            right = mid + 1
            index += 1
        else:
            left = mid - 1
            right = mid

        while right < len(nums):
            res[index] = nums[left]
            index += 1
            res[index] = nums[right]
            index += 1
            left -= 1
            right += 1

        return res


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: two pointers
        """
        nums.sort()
        res = []
        mid = len(nums) >> 1

        if len(nums) % 2:
            res.append(nums[mid])
            left = mid - 1
            right = mid + 1
        else:
            left = mid - 1
            right = mid

        while right < len(nums):
            res.append(nums[left])
            res.append(nums[right])
            left -= 1
            right += 1

        return res


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: build-in function
        """
        nums.sort()
        length = len(nums)
        new_numbers = [0] * length

        new_numbers[: length + 1: 2] = nums[: (length + 1) // 2]
        new_numbers[1: length + 1: 2] = nums[(length + 1) // 2:]

        return new_numbers


print(Solution().rearrangeArray([1, 2, 3, 4, 5]) == [3, 2, 4, 1, 5])
print(Solution().rearrangeArray([1, 2, 3, 4]) == [2, 3, 1, 4])
print(Solution().rearrangeArray([6, 2, 0, 9, 7]) == [6, 2, 7, 0, 9])
print(Solution().rearrangeArray([1, 3, 2]) == [2, 1, 3])
print(Solution().rearrangeArray([15, 7, 13, 6, 3, 11, 14, 1, 20]) == [11, 7, 13, 6, 14, 3, 15, 1, 20])
