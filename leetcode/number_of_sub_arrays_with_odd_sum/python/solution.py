class Solution:
    def numOfSubarrays(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: prefix sum
        """
        MOD = 10**9 + 7
        prefix = 0
        res = 0
        odd_counter = 0
        even_counter = 1

        for num in nums:
            prefix += num

            if prefix % 2:
                res = (res + even_counter) % MOD
                odd_counter += 1
            else:
                res = (res + odd_counter) % MOD
                even_counter += 1

        return res


class Solution:
    def numOfSubarrays(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: brute-force, prefix sum
        """
        MOD = 10**9 + 7
        prefix = [0]
        res = 0

        for num in nums:
            prefix.append(prefix[-1] + num)

        for right in range(len(prefix)):
            res %= MOD

            for left in range(right):
                if (prefix[right] - prefix[left]) % 2:
                    res += 1

        return res


print(Solution().numOfSubarrays([3]) == 1)
print(Solution().numOfSubarrays([1, 3, 5]) == 4)
print(Solution().numOfSubarrays([2, 4, 6]) == 0)
print(Solution().numOfSubarrays([1, 2, 3, 4]) == 6)
print(Solution().numOfSubarrays([1, 2, 3, 4, 5, 6, 7]) == 16)
