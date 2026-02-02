r"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class Solution:
    def romanToInt(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: iteration
        """
        N = len(text)
        value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0

        for char in text:
            res += value[char]

        for index in range(N - 1):
            char = text[index]
            next_char = text[index + 1]
            if (
                char == "I" and next_char in ("VX") or
                char == "X" and next_char in ("LC") or
                char == "C" and next_char in ("DM")
            ):
                res -= 2 * value[text[index]]

        return res


class Solution:
    def romanToInt(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: iteration
        """
        N = len(text)
        res = 0
        value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        index = 0
        while index < N:
            char = text[index]

            if index + 1 == N:
                res += value[char]
                break

            next_char = text[index + 1]

            if value[char] < value[next_char]:
                res += -value[char] + value[next_char]
                index += 2
            else:
                res += value[char]
                index += 1

        return res


print(Solution().romanToInt("III") == 3)
print(Solution().romanToInt("IV") == 4)
print(Solution().romanToInt("V") == 5)
print(Solution().romanToInt("VI") == 6)
print(Solution().romanToInt("IX") == 9)
print(Solution().romanToInt("X") == 10)
print(Solution().romanToInt("XII") == 12)
print(Solution().romanToInt("LVIII") == 58)
print(Solution().romanToInt("MCMXCIV") == 1994)
