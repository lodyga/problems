class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A: iteration
        """
        num_set = set()

        for num in nums:
            if num in num_set:
                num_set.discard(num)
            else:
                num_set.add(num)

        return list(num_set)


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        xor = 0
        
        for num in nums:
            xor ^= num

        diff_bit = 1

        while xor & diff_bit == 0:
            diff_bit <<= 1

        res = [0, 0]

        for num in nums:
            if num & diff_bit:
                res[1] ^= num
            else:
                res[0] ^= num
        
        return res


print(sorted(Solution().singleNumber([1, 2, 1, 3, 2, 5])) == sorted([3, 5]))
print(sorted(Solution().singleNumber([-1, 0])) == sorted([-1, 0]))
print(sorted(Solution().singleNumber([0, 1])) == sorted([0, 1]))
