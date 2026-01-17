r"""
draft
[2, 2, 6, 1]
 2  2  6  1
 2    26  1
 22    6  1
                  .
            /           \
           2            22
        /     \       /
       2      26     6
     /       /     /
    6       1     1
   /
  1

[3, 2, 1, 1, (1)]
{0: 3, 1: 2, 2: 1, 3: 1, 4: 1}
"""


class Solution:
    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: brute-force
        """
        def dfs(index: int) -> int:
            if index == len(text):
                return 1

            num = text[index]
            # (1-9)
            one_digit_num = 0
            if num != "0":
                one_digit_num = dfs(index + 1)
            # (10-26)
            two_digit_num = 0
            if (
                index + 1 < len(text) and
                (num == "1" or
                 (num == "2" and "0" <= text[index + 1] <= "6"))
            ):
                two_digit_num = dfs(index + 2)

            return one_digit_num + two_digit_num

        return dfs(0)

    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        memo = [-1] * (len(text) + 1)
        memo[-1] = 1

        def dfs(index: int) -> int:
            if memo[index] != -1:
                return memo[index]

            num = text[index]
            # (1-9)
            one_digit_num = 0
            if num != "0":
                one_digit_num = dfs(index + 1)
            # (10-26)
            two_digit_num = 0
            if (
                index + 1 < len(text) and
                (num == "1" or
                 (num == "2" and "0" <= text[index + 1] <= "6"))
            ):
                two_digit_num = dfs(index + 2)

            memo[index] = one_digit_num + two_digit_num
            return memo[index]

        return dfs(0)

    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [0] * (len(text) + 1)
        cache[-1] = 1

        for index in range(len(text) - 1, -1, -1):
            num = text[index]
            if num == "0":
                continue
            # (1-9)
            cache[index] += cache[index + 1]
            # (10-26)
            if (
                index + 1 < len(text) and
                (num == "1" or
                 (num == "2" and "0" <= text[index + 1] <= "6"))
            ):
                cache[index] += cache[index + 2]

        return cache[0]

    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [1, 1]

        for index in range(len(text) - 1, -1, -1):
            num = text[index]
            if num == "0":
                cache[1] = cache[0]
                cache[0] = 0
                continue
            # (1-9)
            cache_at_index = cache[0]
            # (10-26)
            if (
                index + 1 < len(text) and
                (num == "1" or
                 (num == "2" and "0" <= text[index + 1] <= "6"))
            ):
                cache_at_index += cache[1]

            cache[1] = cache[0]
            cache[0] = cache_at_index

        return cache[0]


print(Solution().numDecodings("5") == 1)
print(Solution().numDecodings("23") == 2)
print(Solution().numDecodings("226") == 3)
print(Solution().numDecodings("2261") == 3)
print(Solution().numDecodings("12") == 2)
print(Solution().numDecodings("2101") == 1)
print(Solution().numDecodings("06") == 0)
print(Solution().numDecodings("0") == 0)
print(Solution().numDecodings("2617") == 4)
print(Solution().numDecodings("111111111111111111111111111111111111111111111") == 1836311903)
