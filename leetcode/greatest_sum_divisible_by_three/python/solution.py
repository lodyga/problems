class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: 
            A: brute-force
        """
        def dfs(index, total):
            if index == len(nums):
                if total % 3 == 0:
                    return total
                else:
                    return 0

            num = nums[index]
            skip = dfs(index + 1, total)
            take = dfs(index + 1, total + num)
            return max(skip, take)

        return dfs(0, 0)


class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: bottom-up
        """
        # Max subsequence sum divided by 3 with rest 0, 1, 2 respectively.
        cache = [0, 0, 0]

        for num in nums:
            for c in cache.copy():
                mod = (c + num) % 3
                cache[mod] = max(cache[mod], c + num)

        return cache[0]


print(Solution().maxSumDivThree([3]) == 3)
print(Solution().maxSumDivThree([4]) == 0)
print(Solution().maxSumDivThree([3, 6, 5, 1, 8]) == 18)
print(Solution().maxSumDivThree([4]) == 0)
print(Solution().maxSumDivThree([1, 2, 3, 4, 4]) == 12)
print(Solution().maxSumDivThree([366, 809, 6, 792, 822, 181, 210, 588, 344, 618, 341, 410, 121, 864, 191, 749, 637, 169, 123, 472, 358, 908, 235, 914, 322, 946, 738, 754, 908, 272, 267, 326, 587, 267, 803, 281, 586, 707, 94, 627, 724, 469, 568, 57, 103, 984, 787, 552, 14, 545, 866, 494, 263, 157, 479, 823, 835, 100, 495, 773, 729, 921, 348, 871, 91, 386, 183, 979, 716, 806, 639, 290, 612, 322, 289, 910, 484, 300, 195, 546, 499, 213, 8, 623, 490, 473, 603, 721, 793, 418, 551, 331, 598, 670, 960, 483, 154, 317, 834, 352]) == 50487)
