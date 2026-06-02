class Solution:
    def rotate(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: two pointers, in-place method
        """
        def _rotate_inplace(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        N = len(nums)
        k %= N

        _rotate_inplace(0, N - 1)
        _rotate_inplace(0, k - 1)
        _rotate_inplace(k, N - 1)

        return nums


class Solution:
    def rotate(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: two pointers
        """
        N = len(nums)
        k %= N
        pivot = N - k
        res = []

        for idx in range(pivot, N):
            res.append(nums[idx])

        for idx in range(pivot):
            res.append(nums[idx])

        return res


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: build-in function
        """
        N = len(nums)
        pivot = N - k % N
        return nums[pivot: ] + nums[: pivot]


print(Solution().rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3])
print(Solution().rotate([1, 2, 3], 2) == [2, 3, 1])
print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4])
print(Solution().rotate([1, 2, 3, 4, 5, 6], 1) == [6, 1, 2, 3, 4, 5])
print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4])
print(Solution().rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100])
print(Solution().rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], 38) == [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
