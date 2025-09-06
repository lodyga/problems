class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force
        """
        def dfs(index1, index2, prev_letter, prev_char):
            if index1 == len(text):
                return True
            elif index2 == len(pattern):
                return False
            
            letter = text[index1]
            char = pattern[index2]

            if letter == char:
                return dfs(index1 + 1, index2 + 1, letter, char)
            elif char == "*":
                if prev_char == letter:
                    return dfs(index1 + 1, index2, letter, prev_char)
                elif prev_char == ".":
                    return True
                # end pattern, pattern matched
                elif prev_char == prev_letter:
                    return dfs(index1 + 1, index2 + 1, "", "")
                # end pattern, no match
                else:
                    return dfs(index1 - 1, index2 + 1, "", "")

            elif char == ".":
                return dfs(index1 + 1, index2 + 1, letter, char)
            else:
                return dfs(index1 + 1, index2 + 1, letter, char)
        
        return dfs(0, 0, "", "")


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


print(Solution().isMatch("a", "a"), True)
print(Solution().isMatch("aa", "a"), False)
print(Solution().isMatch("a", "aa"), False)
print(Solution().isMatch("aa", "a*"), True)
print(Solution().isMatch("aaaaa", "a*"), True)
print(Solution().isMatch("ab", ".*"), True)
print(Solution().isMatch("b", "a*b"), True)
print(Solution().isMatch("ab", "a*b"), True)
print(Solution().isMatch("aab", "c*a*b"), True)
print(Solution().isMatch("ippi", "p*."), False)
print(Solution().isMatch("mississippi", "mis*is*p*."), False)
print(Solution().isMatch("ippi", "ip*."), True)
print(Solution().isMatch("mississippi", "mis*is*ip*."), True)
print(Solution().isMatch("", "b*"), True)