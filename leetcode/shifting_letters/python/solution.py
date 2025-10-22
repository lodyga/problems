class Solution:
    def shiftingLetters(self, text: str, shifts: list[int]) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: prefix sum
        """
        def shift_letter(letter, shift):
            letter_index = ord(letter) - ord("a")
            shifted_index = letter_index + shift
            return chr(shifted_index % 26 + ord("a"))

        letters = list(text)
        shift = 0  # prefix sum
        
        for index in reversed(range(len(text))):
            letter = text[index]
            shift += shifts[index]
            letters[index] = shift_letter(letter, shift)
        
        return "".join(letters)


print(Solution().shiftingLetters("abc", [3, 5, 9]) == "rpl")
print(Solution().shiftingLetters("aaa", [1, 2, 3]) == "gfd")