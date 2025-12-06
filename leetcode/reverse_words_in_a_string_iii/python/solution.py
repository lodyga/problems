class Solution:
    def reverseWords(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: iteration, build-in function
        """
        words = []
        for word in text.split(" "):
            words.append(word[::-1])
        return " ".join(words)


class Solution:
    def reverseWords(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: build-in function
        """
        return " ".join(word[::-1] for word in text.split(" "))


class Solution:
    def reverseWords(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack, list
            A: iteration
        """
        letter_stack = []
        words = []

        for letter in text:
            if letter == " ":
                words.append("".join(reversed(letter_stack)))
                letter_stack = []
            else:
                letter_stack.append(letter)
        
        if letter_stack:
            words.append("".join(reversed(letter_stack)))
        return " ".join(words)


class Solution:
    def reverseWords(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: two pointers
        """
        def reverse_word(left, right):
            while left < right:
                letters[left], letters[right] = letters[right], letters[left]
                left += 1
                right -= 1

        letters = list(text)
        left = 0
        for right, letter in enumerate(letters):
            if letter == " " or right == len(text) - 1:
                reverse_word(left, right if right == len(text) - 1 else right - 1)
                left = right + 1
        return "".join(letters)


print(Solution().reverseWords("Let's take LeetCode contest")== "s'teL ekat edoCteeL tsetnoc")
print(Solution().reverseWords("Mr Ding") == "rM gniD")
print(Solution().reverseWords("hehhhhhhe") == "ehhhhhheh")
