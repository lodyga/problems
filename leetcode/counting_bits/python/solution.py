class Solution:
    def countBits(self, num: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: bit manipulation, bottom-up
        """
        res = [0]

        while True:
            for idx in range(len(res)):
                if len(res) == num + 1:
                    return res

                res.append(res[idx] + 1)


class Solution:
    def countBits(self, num: int) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: bit manipulation
        """
        def count_set_bits(num):
            res = 0
            while num:
                res += num & 1
                num = num >> 1
            return res

        bits_array = [count_set_bits(idx)
                      for idx in range(1, num + 1)]

        bits_array.insert(0, 0)
        return bits_array


class Solution:
    def countBits(self, n: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
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
            DS: array
            A: bit manipulation, built-in function
        """
        return [bin(i).count("1")
                for i in range(n + 1)]


print(Solution().countBits(2) == [0, 1, 1])
print(Solution().countBits(5) == [0, 1, 1, 2, 1, 2])
print(Solution().countBits(0) == [0])
print(Solution().countBits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1])
