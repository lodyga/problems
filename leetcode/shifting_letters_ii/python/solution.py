class Solution:
    def shiftingLetters(self, text: str, shifts: list[list[int]]) -> str:
        """
        Time complexity: O(n + s)
            n: text length
            s: shifts length
        Auxiliary space complexity: O(n)
        Tags:
            DS: array, string
            A: prefix sum
        """
        A = ord("a")
        letter_vals = [ord(letter) - A for letter in text]
        suffix = [0] * len(text)
        shift = 0

        for start, end, direction in shifts:
            suffix[end] += 1 if direction else - 1

            if start:
                suffix[start - 1] += -1 if direction else 1

        for index in range(len(text) - 1, -1, -1):
            shift += suffix[index]
            letter_vals[index] += shift

        return "".join(chr(letter_val % 26 + A)
                       for letter_val in letter_vals)


print(Solution().shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace")
print(Solution().shiftingLetters("dztz", [[0, 0, 0], [1, 1, 1]]) == "catz")
