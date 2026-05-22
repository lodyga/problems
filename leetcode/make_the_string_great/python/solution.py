class Solution:
    def makeGood(self, text: str) -> str:
        stack = []

        for letter in text:
            if (
                stack and
                stack[-1] != letter and
                stack[-1].upper() == letter.upper()
            ):
                stack.pop()
            else:
                stack.append(letter)

        return "".join(stack)


print(Solution().makeGood("leEeetcode") == "leetcode")
print(Solution().makeGood("abBAcC") == "")
print(Solution().makeGood("s") == "s")
print(Solution().makeGood("Mc") == "Mc")
print(Solution().makeGood("Pp") == "")
