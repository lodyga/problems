class Solution:
    def shiftingLetters(self, text: str, shifts: list[int]) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: prefix sum
        """
        letters = list(text)
        shift = 0

        for index in range(len(text) - 1, -1, -1):
            shift += shifts[index]
            letter = letters[index]
            letters[index] = chr(
                ((ord(letter) - ord("a") + shift) % 26) +
                ord("a")
            )

        return "".join(letters)


print(Solution().shiftingLetters("abc", [3, 5, 9]) == "rpl")
print(Solution().shiftingLetters("aaa", [1, 2, 3]) == "gfd")
