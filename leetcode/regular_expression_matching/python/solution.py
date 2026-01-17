class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: top-down
            regex
        """
        memo = [[-1] * len(pattern) for _ in range(len(text))]

        def dfs(index1: int, index2: int) -> int:
            if index2 == len(pattern):
                return index1 == len(text)
            elif index1 == len(text):
                # capute all of trailing x* groups to match the empty string:
                while index2 + 1 < len(pattern) and pattern[index2 + 1] == "*":
                    index2 += 2
                return index2 == len(pattern)
            elif memo[index1][index2] != -1:
                return memo[index1][index2]

            letter = text[index1]
            char = pattern[index2]
            next_char = pattern[index2 + 1] \
                if index2 + 1 < len(pattern) else ""

            res = 0
            if next_char == "*":
                # Skip current pattrn.
                if dfs(index1, index2 + 2):
                    res = 1
                # Match one letter.
                elif char in (letter, "."):
                    # use parrtern
                    if dfs(index1 + 1, index2):
                        res = 1

            elif char in (letter, "."):
                res = dfs(index1 + 1, index2 + 1)

            memo[index1][index2] = res
            return res

        return bool(dfs(0, 0))


class Solution:
    def isMatch(self, text: str, regexp: str) -> bool:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string
            A: iteration
            regex
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


class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: top-down
            regex
        """
        memo = [[-1] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        def dfs(index1: int, index2: int) -> int:
            if index2 == len(pattern):
                return index1 == len(text)
            elif memo[index1][index2] != -1:
                return memo[index1][index2]

            is_letter_matched = index1 < len(text) and \
                (pattern[index2] in (".", text[index1]))
            # is_letter_matched = pattern[index2] == "."
            # if index1 < len(text):
            #     is_letter_matched |= pattern[index2] == text[index1]
            is_star_next = index2 + 1 < len(pattern) and \
                pattern[index2 + 1] == "*"

            res = 0
            if is_star_next:
                # Skip current pattrn.
                if dfs(index1, index2 + 2):
                    res = 1
                # if letter matched and use parrtern
                elif is_letter_matched and dfs(index1 + 1, index2):
                    res = 1

            elif is_letter_matched:
                res = dfs(index1 + 1, index2 + 1)

            memo[index1][index2] = res
            return res

        return bool(dfs(0, 0))


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
