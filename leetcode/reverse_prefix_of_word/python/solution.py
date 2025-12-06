class Solution:
    def reversePrefix(self, word: str, pivot: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        letter_stack = []
        for index, letter in enumerate(word):
            letter_stack.append(letter)
            if letter == pivot:
                return "".join(reversed(letter_stack)) + word[index + 1:]
        return word


class Solution:
    def reversePrefix(self, word: str, pivot: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: iteration
        """
        for index, letter in enumerate(word):
            if letter == pivot:
                return "".join(reversed(word[: index + 1])) + word[index + 1:]
        return word


print(Solution().reversePrefix("abcdefd", "d") == "dcbaefd")
print(Solution().reversePrefix("xyxzxe", "z") == "zxyxxe")
print(Solution().reversePrefix("abcd", "z") == "abcd")
