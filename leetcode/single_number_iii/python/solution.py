class Solution:
    def singleNumber(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        number_set = set()

        for number in numbers:
            if number in number_set:
                number_set.remove(number)
            else:
                number_set.add(number)
        
        return list(number_set)


class Solution:
    def singleNumber(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: bit manipulation
        """
        two_xor = 0

        for number in numbers:
            two_xor ^= number
        
        diff_bit = 1
        while (diff_bit & two_xor) == 0:
            diff_bit <<= 1

        zeros = 0
        ones = 0

        for number in numbers:
            if diff_bit & number:
                ones ^= number
            else:
                zeros ^= number

        return [zeros, ones]


print(Solution().singleNumber([1, 2, 1, 3, 2, 5]), [3, 5])
print(Solution().singleNumber([-1, 0]), [-1, 0])
print(Solution().singleNumber([0, 1]), [0, 1])