class Solution:
    def reverseWords(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: iteration, build-in function
        """
        res = []

        for word in text.split():
            res.append(word[::-1])

        return " ".join(res)


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
        res = []
        stack = []

        for char in text + " ":
            if char == " ":
                res.append("".join(reversed(stack)))
                stack.clear()
            else:
                stack.append(char)

        return " ".join(res)


print(Solution().reverseWords("Let's take LeetCode contest")== "s'teL ekat edoCteeL tsetnoc")
print(Solution().reverseWords("Mr Ding") == "rM gniD")
print(Solution().reverseWords("hehhhhhhe") == "ehhhhhheh")
