class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(k)
        Tags:
            DS: hash map
            A: prefix sum
        """
        # prefix sum mod
        mod = 0
        seen = {0: 1}
        res = 0

        for num in nums:
            if num < 0:
                num = num % k

            mod = (mod + num) % k

            if mod in seen:
                res += seen[mod]
                seen[mod] += 1
            else:
                seen[mod] = 1

        return res


print(Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5) == 7)
print(Solution().subarraysDivByK([5], 9) == 0)
print(Solution().subarraysDivByK([-1, 2, 9], 2) == 2)
print(Solution().subarraysDivByK([7, 4, -10], 5) == 1)
