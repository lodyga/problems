class Solution:
    def countBits(self, num: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: bit manipulation, bottom-up
        """
        res = [0]

        while True:
            for index in range(len(res)):
                if len(res) == num + 1:
                    return res
                res.append(res[index] + 1)


class Solution:
    def countBits(self, number: int) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        def count_set_bits(number):
            set_bit_counter = 0
            while number:
                set_bit_counter += number & 1
                number = number >> 1
            return set_bit_counter

        bits_array = [0] * (number + 1)

        for index in range(1, number + 1):
            bits_array[index] = count_set_bits(index)

        return bits_array


class Solution:
    def countBits(self, n: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation, bottom-up
        """
        cache = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            cache[i] = 1 + cache[i - offset]
        return cache


class Solution:
    def countBits(self, n: int) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        return [bin(i).count("1") for i in range(n + 1)]


print(Solution().countBits(0) == [0])
print(Solution().countBits(2) == [0, 1, 1])
print(Solution().countBits(5) == [0, 1, 1, 2, 1, 2])
print(Solution().countBits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1])
