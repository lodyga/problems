class Solution:
    def shiftingLetters(self, text: str, shifts: list[list[int]]) -> str:
        """
        Time complexity: O(n + s)
            n: text length
            s: shifts length
        Auxiliary space complexity: O(n + s)
        Tags: prefix sum
        """
        def shift_letter(letter, shift):
            letter_index = ord(letter) - ord("a")
            shifted_index = letter_index + shift
            return chr(shifted_index % 26 + ord("a"))
        
        shift_sum = [0] * (len(text) + 1)
        for start, end, direction in shifts:
            shift_sum[end + 1] += 1 if direction else -1
            shift_sum[start] += -1 if direction else 1
        
        letters = list(text)
        for index in reversed(range(len(shift_sum) - 1)):
            shift_sum[index] += shift_sum[index + 1]
            letters[index] = shift_letter(letters[index], shift_sum[index + 1])

        return "".join(letters)


class Solution:
    def shiftingLetters(self, text: str, shifts: list[list[int]]) -> str:
        """
        Time complexity: O(n * s)
            n: text length
            s: shifts length
        Auxiliary space complexity: O(n)
        Tags: brute force
        """
        def shift_letter(letter, shift):
            letter_index = ord(letter) - ord("a")
            shifted_index = letter_index + shift
            return chr(shifted_index % 26 + ord("a"))

        shift_sum = [0] * len(text)
        for start, end, direction in shifts:
            for index in range(start, end + 1):
                shift_sum[index] += 1 if direction else -1
        
        letters = list(text)
        for index, letter in enumerate(text):
            letters[index] = shift_letter(letter, shift_sum[index])
        
        return "".join(letters)


print(Solution().shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace")
print(Solution().shiftingLetters("dztz", [[0, 0, 0], [1, 1, 1]]) == "catz")