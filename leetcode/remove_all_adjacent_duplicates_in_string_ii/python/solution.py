class Solution:
    def removeDuplicates(self, text: str, k: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        # [(letter, frequency), ]
        stack = []

        for letter in text:
            if stack and stack[-1][0] == letter:
                _, freq = stack.pop()

                if freq + 1 != k:
                    stack.append((letter, freq + 1))
            else:
                stack.append((letter, 1))

        return "".join(letter * freq 
                       for letter, freq in stack)


print(Solution().removeDuplicates("abcd", 2) == "abcd")
print(Solution().removeDuplicates("deeedbbcccbdaa", 3) == "aa")
print(Solution().removeDuplicates("pbbcggttciiippooaais", 2) == "ps")
