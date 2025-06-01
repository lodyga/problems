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


class Solution:
    def minFlips(self, numbers: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: brute-force
        """
        min_flip_a = len(numbers)
        min_flip_b = len(numbers)
        
        target_a = "".join(str(i % 2) 
                           for i in range(len(numbers)))
        target_b = "".join(str((i + 1) % 2) 
                           for i in range(len(numbers)))

        for _ in range(len(numbers)):
            numbers = numbers[1:] + numbers[0]
            flip_a = 0
            flip_b = 0

            for index, number in enumerate(numbers):
                if number != target_a[index]:
                    flip_a += 1

                if number != target_b[index]:
                    flip_b += 1

            min_flip_a = min(min_flip_a, flip_a)
            min_flip_b = min(min_flip_b, flip_b)
        
        return min(min_flip_a, min_flip_b)


print(Solution().minFlips("111000") == 2)
print(Solution().minFlips("010") == 0)
print(Solution().minFlips("1110") == 1)
print(Solution().minFlips("01001001101") == 2)