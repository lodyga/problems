class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        def dfs(index1, index2):
            if index2 == len(pattern):
                return index1 == len(text)
            elif index1 == len(text):
                return index2 + 2 == len(pattern) and pattern[index2 + 1] == "*"
            
            letter = text[index1] if index1 < len(text) else ""
            char = pattern[index2]
            next_char = pattern[index2 + 1] if index2 + 1 < len(pattern) else ""
            
            if next_char == "*":
                # skip current pattern
                if dfs(index1, index2 + 2):
                    return True
                # match one letter
                if letter == char or char == ".":
                    if dfs(index1 + 1, index2):
                        return True
                return False
            elif letter == char:
                return dfs(index1 + 1, index2 + 1)
            elif char == ".":
                return dfs(index1 + 1, index2 + 1)

            return False
        
        return dfs(0, 0)


class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        def dfs(index1, index2):
            if index2 == len(pattern):
                return index1 == len(text)
            elif index1 == len(text):
                return index2 + 2 == len(pattern) and pattern[index2 + 1] == "*"
            
            letter = text[index1] if index1 < len(text) else ""
            char = pattern[index2]
            next_char = pattern[index2 + 1] if index2 + 1 < len(pattern) else ""
            
            if next_char == "*":
                if (
                    letter == char or 
                    char == "."
                ):
                    return (
                        # skip text letter
                        dfs(index1 + 1, index2)
                        # skip `.*` pattern
                        or dfs(index1, index2 + 2)
                    )
                elif char.isalpha():
                    return dfs(index1, index2 + 2)
            elif letter == char:
                return dfs(index1 + 1, index2 + 1)
            elif char == ".":
                return dfs(index1 + 1, index2 + 1)

            return False
        
        return dfs(0, 0)


class Solution:
    def isMatch(self, text: str, regexp: str) -> bool:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: regex
        """
        def match_star(char: str, regexp: str, text: str) -> bool:
            while True:
                if match_here(regexp, text):
                    return True
                elif len(text) == 0 or char not in (text[0], "."):
                    break
                text = text[1:]
            return False

        def match_here(regexp, text):
            if len(regexp) == 0:
                return len(text) == 0
            # elif regexp and len(text) == 0:
            #     return False
            elif len(regexp) > 1 and regexp[1] == "*":
                return match_star(regexp[0], regexp[2:], text)
            elif text and (regexp[0] == '.' or regexp[0] == text[0]):
                return match_here(regexp[1:], text[1:])
            return False

        return match_here(regexp, text)


print(Solution().isMatch("a", "a") == True)
print(Solution().isMatch("aa", "a") == False)
print(Solution().isMatch("a", "aa") == False)
print(Solution().isMatch("aa", "a*") == True)
print(Solution().isMatch("ab", "a*") == False)
print(Solution().isMatch("aaaaa", "a*") == True)
print(Solution().isMatch("ab", ".*") == True)
print(Solution().isMatch("b", "a*b") == True)
print(Solution().isMatch("ab", "a*b") == True)
print(Solution().isMatch("aab", "c*a*b") == True)
print(Solution().isMatch("ippi", "p*.") == False)
print(Solution().isMatch("mississippi", "mis*is*p*.") == False)
print(Solution().isMatch("ipp", "ip*") == True)
print(Solution().isMatch("ippi", "ip*.") == True)
print(Solution().isMatch("mississippi", "mis*is*ip*.") == True)
print(Solution().isMatch("", "b*") == True)
print(Solution().isMatch("ab", ".*c") == False)
print(Solution().isMatch("abc", ".*c") == True)
print(Solution().isMatch("aaa", "a*a") == True)
print(Solution().isMatch("aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*") == True)