class Solution:
    def removeDuplicates(self, text: str, k: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        stack = []  # [[letter, frequency], ]

        for letter in text:
            if (stack and
                stack[-1][0] == letter):
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
            else:
                stack.append([letter, 1])

        return "".join(letter * frequency 
                       for letter, frequency in stack)


class Solution:
    def removeDuplicates(self, text: str, k: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        stack = []  # [(letter, frequency), ]

        for letter in text:
            if (stack and
                stack[-1][0] == letter and
                    stack[-1][1] == k - 1):
                for _ in range(k - 1):
                    stack.pop()
            elif (stack and
                  stack[-1][0] == letter):
                stack.append((letter, stack[-1][1] + 1))
            else:
                stack.append((letter, 1))

        return "".join(letter for letter, _ in stack)  # "".join(map(lambda x: x[0], stack))


print(Solution().removeDuplicates("abcd", 2) == "abcd")
print(Solution().removeDuplicates("deeedbbcccbdaa", 3) == "aa")
print(Solution().removeDuplicates("pbbcggttciiippooaais", 2) == "ps")