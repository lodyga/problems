class Solution:
    def reverseParentheses(self, text: str) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: brute-force
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
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        stack = []
        chunk = ""

        for char in text:
            if char == "(":
                stack.append(chunk)
                chunk =  ""
            elif char == ")":
                chunk = stack.pop() + chunk[::-1]
            else:
                chunk += char
        
        return chunk


class Solution2:
    def reverseParentheses(self, text: str) -> str:
        """
        Time complexity: O(n2)
            O(n*m)
            n: text length
            m: parenthesis pairs count
        Auxiliary space complexity: O(n)
        Tags: stack
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


print(Solution().reverseParentheses("yfgnxf") == "yfgnxf")
print(Solution().reverseParentheses("x(ab)z") == "xbaz")
print(Solution().reverseParentheses("(abcd)") == "dcba")
print(Solution().reverseParentheses("(u(love)i)") == "iloveu")
print(Solution().reverseParentheses("(ed(et(oc))el)") == "leetcode")
print(Solution().reverseParentheses("a(bcdefghijkl(mno)p)q") == "apmnolkjihgfedcbq")
print(Solution().reverseParentheses("ta()usw((((a))))") == "tauswa")
print(Solution().reverseParentheses("s()uteawj((eg))") == "suteawjeg")
