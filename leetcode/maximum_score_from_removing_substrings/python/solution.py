class Solution:
    def maximumGain(self, text: str, x: int, y: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: greedy, stack
        """
        stack = []
        rev_stack = []
        points = 0

        for letter in text:
            if y > x and stack and stack[-1] == "b" and letter == "a":
                points += y
                stack.pop()
            elif x > y and stack and stack[-1] == "a" and letter == "b":
                points += x
                stack.pop()
            else:
                stack.append(letter)
        
        index = len(stack) - 1
        while index > -1:
            if (
                rev_stack and rev_stack[-1] == "a" and 
                stack[-1] == "b"
            ):
                points += y
                stack.pop()
                rev_stack.pop()
            elif (
                rev_stack and rev_stack[-1] == "b" and 
                stack[-1] == "a"
            ):
                points += x
                stack.pop()
                rev_stack.pop()
            else:
                rev_stack.append(stack.pop())

            index -= 1

        return points


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


print(Solution().maximumGain("aba", 4, 5) == 5)
print(Solution().maximumGain("bab", 4, 5) == 5)
print(Solution().maximumGain("cdbcbbaaabab", 4, 5) == 19)
print(Solution().maximumGain("aabbaaxybbaabb", 5, 4) == 20)
print(Solution().maximumGain("aabbrtababbabmaaaeaabeawmvaataabnaabbaaaybbbaabbabbbjpjaabbtabbxaaavsmmnblbbabaeuasvababjbbabbabbasxbbtgbrbbajeabbbfbarbagha", 8484, 4096) == 198644)
print(Solution().maximumGain("babeaaabbafaaabbnaabuaaaaagabbaabbbbbmaaanaasaebbvlaaabbbaibabbbabaaabasbbryqraryobuabguabaabbmabgubabbaaraaaabapbaabsbbbbbbbbahabbbsanaajbabarbntbqagkbababbabbbbaabaybagababaabbzaaaaaaambwabbbaababmxqbbgbabbbabbbbbaakabaabzabbabfabjbobabaaaabbbaaaaaaaajbbbaqrabnarsaabbbaabaabavgbaaabtmcbbababbbubaaababaedbbtabbalkababiaaaabbaafabaabtvbbzayaaaakzbdafbasbaabbsbbarbebaaboyabbabnyamabbbfubaaebabaababbbbbqxajaaaamfabbabbbapbubaabbehbbnaandabmxbqcaaqbyaabbamafbaufaabblbbbbabbaabgbdbbnbaababaiauaybbtnbnaayasgafadbabblabbbaababbtsbabapbdaaasxxafakaaaaabrbbcabaahzbaaajbbbbbhaabbabbtbababbababaxabaaaipabbxbaagbaaabba", 7275, 9407) == 1220161)