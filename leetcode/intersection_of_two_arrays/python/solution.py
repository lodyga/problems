class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set, list
            A: build-in function
        """
        return list(set(nums1) & set(nums2))


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set, list
        """
        num1_set = set(nums1)
        res = []
        
        for num in nums2:
            if num in num1_set:
                res.append(num)
                num1_set.remove(num)
        return res


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array, list
            A: iteration
        """
        num_freq1 = [0] * 1001
        num_freq2 = [0] * 1001

        for num in nums1:
            num_freq1[num] += 1
        
        for num in nums2:
            num_freq2[num] += 1

        res = []
        for num in range(len(num_freq1)):
            freq1 = num_freq1[num]
            freq2 = num_freq2[num]

            if freq1 and freq2:
                res.append(num)

        return res


print(sorted(Solution().intersection([1, 2, 2, 1], [2, 2])) == sorted([2]))
print(sorted(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4])) == sorted([4, 9]))
