class Solution:
    def reverseParentheses(self, text: str) -> str:
        """
        Time complexity: O(n2)
            O(n*m)
            n: text length
            m: parenthesis pairs count
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
        """
        stack = []
        res = ""

        for char in text:
            if char == "(":
                stack.append(res)
                res = ""
            elif char == ")":
                res = stack.pop() + res[::-1]
            else:
                res += char

        return res


class Solution:
    def reverseParentheses(self, text: str) -> str:
        """
        Time complexity: O(n2)
            O(n*m)
            n: text length
            m: parenthesis pairs count
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: brute-force
        """
        stack = []

        for char in text:
            if char == ")":
                chunk = []
                while stack[-1] != "(":
                    chunk.append(stack.pop())
                stack.pop()
                stack.extend(chunk)
            else:
                stack.append(char)

        return "".join(stack)


class Solution:
    def reverseParentheses(self, text: str) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            A: brute-force
        """
        def dfs(text):
            res = ""
            index = 0
            while index < len(text):
                char = text[index]
                if char == "(":
                    opened = 1
                    index += 1
                    to_reverse = ""

                    while opened:
                        char = text[index]
                        to_reverse += char
                        if char == "(":
                            opened += 1
                        elif char == ")":
                            opened -= 1
                        index += 1
                    res += dfs(to_reverse[:-1])[::-1]

                else:
                    res += char
                    index += 1
            return res

        return dfs(text)


class Solution:
    def reverseParentheses(self, text: str) -> str:
        """
        Failed
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: two pointers
        """
        left = 0
        right = len(text) - 1
        left_part = []
        right_part = []
        is_reversed = False

        while left <= right:
            while left <= right and text[left] not in "()":
                if is_reversed:
                    right_part.append(text[left])
                else:
                    left_part.append(text[left])
                left += 1
            left += 1

            while left <= right and text[right] not in "()":
                if is_reversed:
                    left_part.append(text[right])
                else:
                    right_part.append(text[right])
                right -= 1
            right -= 1

            is_reversed = not is_reversed

        return "".join(left_part + right_part[::-1])


print(Solution().reverseParentheses("yfgnxf") == "yfgnxf")
print(Solution().reverseParentheses("x(ab)z") == "xbaz")
print(Solution().reverseParentheses("(abcd)") == "dcba")
print(Solution().reverseParentheses("(u(love)i)") == "iloveu")
print(Solution().reverseParentheses("(ed(et(oc))el)") == "leetcode")
print(Solution().reverseParentheses("a(bcdefghijkl(mno)p)q") == "apmnolkjihgfedcbq")
print(Solution().reverseParentheses("ta()usw((((a))))") == "tauswa")
print(Solution().reverseParentheses("s()uteawj((eg))") == "suteawjeg")
print(Solution().reverseParentheses("sxmdll(q)eki(x)") == "sxmdllqekix")
