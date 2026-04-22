class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute force
        """
        N = len(nums)
        counter = 0

        for right in range(N):
            for left in range(right):
                if right - left != nums[right] - nums[left]:
                    counter += 1

        return counter


class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: iteration
        """
        N = len(nums)
        diff_map = {}

        for index, num in enumerate(nums):
            diff = num - index

            if diff not in diff_map:
                diff_map[diff] = []

            diff_map[diff].append(index)

        total_pairs = (N - 1) * N // 2
        arr = (len(vals) for vals in diff_map.values() if len(vals) > 1)
        good_pairs = sum((val - 1) * val // 2 for val in arr)

        return total_pairs - good_pairs


print(Solution().countBadPairs([4, 1, 3, 3]) == 5)
print(Solution().countBadPairs([1, 2, 3, 4, 5]) == 0)
