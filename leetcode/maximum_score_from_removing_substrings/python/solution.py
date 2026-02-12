class Solution:
    def maximumGain(self, text: str, x: int, y: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: stack, string
            A: greedy, iteration
        """
        high_substr, low_substr = ("ab", "ba") if (x >= y) else ("ba", "ab")
        high_pts, low_pts = (x, y) if (x >= y) else (y, x)
        score = 0
        high_stack = []
        
        for char in text:
            if (
                high_stack and
                high_stack[-1] == high_substr[0] and
                char == high_substr[1]
            ):
                high_stack.pop()
                score += high_pts
            else:
                high_stack.append(char)

        low_stack = []
        
        for char in high_stack:
            if (
                low_stack and
                low_stack[-1] == low_substr[0] and
                char == low_substr[1]
            ):
                low_stack.pop()
                score += low_pts
            else:
                low_stack.append(char)

        return score


print(Solution().maximumGain("aba", 4, 5) == 5)
print(Solution().maximumGain("bab", 4, 5) == 5)
print(Solution().maximumGain("cdbcbbaaabab", 4, 5) == 19)
print(Solution().maximumGain("aabbaaxybbaabb", 5, 4) == 20)
print(Solution().maximumGain("aabbrtababbabmaaaeaabeawmvaataabnaabbaaaybbbaabbabbbjpjaabbtabbxaaavsmmnblbbabaeuasvababjbbabbabbasxbbtgbrbbajeabbbfbarbagha", 8484, 4096) == 198644)
print(Solution().maximumGain("babeaaabbafaaabbnaabuaaaaagabbaabbbbbmaaanaasaebbvlaaabbbaibabbbabaaabasbbryqraryobuabguabaabbmabgubabbaaraaaabapbaabsbbbbbbbbahabbbsanaajbabarbntbqagkbababbabbbbaabaybagababaabbzaaaaaaambwabbbaababmxqbbgbabbbabbbbbaakabaabzabbabfabjbobabaaaabbbaaaaaaaajbbbaqrabnarsaabbbaabaabavgbaaabtmcbbababbbubaaababaedbbtabbalkababiaaaabbaafabaabtvbbzayaaaakzbdafbasbaabbsbbarbebaaboyabbabnyamabbbfubaaebabaababbbbbqxajaaaamfabbabbbapbubaabbehbbnaandabmxbqcaaqbyaabbamafbaufaabblbbbbabbaabgbdbbnbaababaiauaybbtnbnaayasgafadbabblabbbaababbtsbabapbdaaasxxafakaaaaabrbbcabaahzbaaajbbbbbhaabbabbtbababbababaxabaaaipabbxbaagbaaabba", 7275, 9407) == 1220161)


class Solution:
    def maximumGain(self, text: str, x: int, y: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map, mle
        """
        stack = []
        memo = {}
        
        def dfs(index, points):
            if index == len(text):
                return points
            elif (index, points) in memo:
                return memo[(index, points)]
            
            letter = text[index]
            ab = ba = skip = 0

            # right letters
            if (
                stack and stack[-1] == "a" and 
                letter == "b"
            ):
                stack.pop()
                ab = dfs(index + 1, points + x)
                stack.append("a")
            elif (
                stack and stack[-1] == "b" and 
                letter == "a"
            ):
                stack.pop()
                ba = dfs(index + 1, points + y)
                stack.append("b")
                
            # skip checking, stack a letter
            stack.append(letter)
            skip = dfs(index + 1, points)
            stack.pop()

            memo[(index, points)] = max(ab, ba, skip)
            return memo[(index, points)]
        
        return dfs(0, 0)


class Solution:
    def maximumGain(self, text: str, x: int, y: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n2)
        Tags: brute-force, tle
        """
        stack = []
        
        def dfs(index):
            if index == len(text):
                return 0
            
            letter = text[index]
            ab = ba = skip = 0

            # right letters
            if (
                stack and stack[-1] == "a" and 
                letter == "b"
            ):
                stack.pop()
                ab = x + dfs(index + 1)
                stack.append("a")
            elif (
                stack and stack[-1] == "b" and 
                letter == "a"
            ):
                stack.pop()
                ba = y + dfs(index + 1)
                stack.append("b")
                
            # skip checking, stack a letter
            stack.append(letter)
            skip = dfs(index + 1)
            stack.pop()

            return max(ab, ba, skip)
        
        return dfs(0)


