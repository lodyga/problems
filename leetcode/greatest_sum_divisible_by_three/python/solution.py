class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: heap, list
            A: greedy
        """
        import heapq
        total = sum(nums)

        if total % 3 == 0:
            return total

        remainder = total % 3
        one = []
        two = []

        for num in nums:
            if num % 3 == 1:
                if len(one) < 2:
                    heapq.heappush(one, -num)
                else:
                    heapq.heappushpop(one, -num)
            elif num % 3 == 2:
                if len(two) < 2:
                    heapq.heappush(two, -num)
                else:
                    heapq.heappushpop(two, -num)

        one = sorted([-num for num in one])
        two = sorted([-num for num in two])
        res = 0

        if remainder == 1:
            if one:
                res = total - one[0]
            if len(two) > 1:
                res = max(res, total - two[0] - two[1])
        elif remainder == 2:
            if two:
                res = total - two[0]
            if len(one) > 1:
                res = max(res, total - one[0] - one[1])

        return res


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
print(Solution().maxSumDivThree([3, 1, 1]) == 3)
print(Solution().maxSumDivThree([3, 6, 5, 1, 8]) == 18)
print(Solution().maxSumDivThree([1, 2, 3, 4, 4]) == 12)
print(Solution().maxSumDivThree([366, 809, 6, 792, 822, 181, 210, 588, 344, 618, 341, 410, 121, 864, 191, 749, 637, 169, 123, 472, 358, 908, 235, 914, 322, 946, 738, 754, 908, 272, 267, 326, 587, 267, 803, 281, 586, 707, 94, 627, 724, 469, 568, 57, 103, 984, 787, 552, 14, 545, 866, 494, 263, 157, 479, 823, 835, 100, 495, 773, 729, 921, 348, 871, 91, 386, 183, 979, 716, 806, 639, 290, 612, 322, 289, 910, 484, 300, 195, 546, 499, 213, 8, 623, 490, 473, 603, 721, 793, 418, 551, 331, 598, 670, 960, 483, 154, 317, 834, 352]) == 50487)
print(Solution().maxSumDivThree([456, 963, 755, 656, 119, 682, 660, 305, 115, 594, 786, 646, 153, 869, 889, 56, 531, 536, 974, 667, 777, 881, 301, 54, 358, 447, 830, 585, 992, 819, 725, 66, 147, 598, 655, 771, 516, 978, 806, 768, 865, 617, 259, 486, 478, 434, 650, 430, 701, 72, 118, 194, 902, 636, 187, 919, 640, 87, 383, 787, 815, 864, 191, 769, 125, 406, 228, 171, 451, 641, 955, 197, 980, 475, 503, 600, 81, 87, 921, 862, 581, 623, 561, 429, 130, 91, 753, 480, 329, 734, 533, 181, 851, 908, 442, 133, 944, 449, 85, 560]) == 53394)
print(Solution().maxSumDivThree([2, 6, 2, 2, 7]) == 15)
