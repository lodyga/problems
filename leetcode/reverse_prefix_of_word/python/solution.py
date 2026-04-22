class Solution:
    def reversePrefix(self, word: str, target_char: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: two pointers
        """
        res = []
        target_idx = -1

        for idx in range(len(word)):
            if word[idx] == target_char:
                target_idx = idx
                break

        for idx in range(target_idx, -1, -1):
            res.append(word[idx])

        for idx in range(target_idx + 1, len(word)):
            res.append(word[idx])

        return "".join(res)


class Solution:
    def reversePrefix(self, word: str, target_char: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        letter_stack = []
        
        for idx, letter in enumerate(word):
            letter_stack.append(letter)

            if letter == target_char:
                return "".join(reversed(letter_stack)) + word[idx + 1:]

        return word


class Solution:
    def reversePrefix(self, word: str, target_char: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: iteration
        """
        for idx, letter in enumerate(word):
            if letter == target_char:
                return "".join(reversed(word[: idx + 1])) + word[idx + 1:]
        return word


print(Solution().reversePrefix("abcdefd", "d") == "dcbaefd")
print(Solution().reversePrefix("xyxzxe", "z") == "zxyxxe")
print(Solution().reversePrefix("abcd", "z") == "abcd")
