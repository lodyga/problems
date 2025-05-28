r"""
blueprint
111000 numbers
010101 target A
101010 target B
"""


class Solution:
    def minFlips(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        left = 0
        text_length = len(text)
        flip_01 = flip_10 = 0
        min_flips = text_length

        for right in range(2 * text_length):
            digit = text[right % text_length]

            if digit == str(right % 2):
                flip_10 += 1
            else:
                flip_01 += 1

            if right - left + 1 == text_length:
                min_flips = min(min_flips, flip_01, flip_10)

                # early exit when there are no flips
                if min_flips == 0:
                    return 0

                if text[left % text_length] == str(left % 2):
                    flip_10 -= 1
                else:
                    flip_01 -= 1
                left += 1

        return min_flips


print(Solution().minFlips("111000") == 2)
print(Solution().minFlips("010") == 0)
print(Solution().minFlips("1110") == 1)
print(Solution().minFlips("01001001101") == 2)