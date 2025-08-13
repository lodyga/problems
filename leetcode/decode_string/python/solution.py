class Solution:
    def decodeString(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        multiplier = 0
        word = ""
        stack = []
        
        for char in text:
            if char.isdigit():
                multiplier = 10 * multiplier + int(char)
            elif char == "[":
                stack.append(word)
                word = ""
                stack.append(multiplier)
                multiplier = 0
            elif char == "]":
                stack_multipilier = stack.pop()
                stack_word = stack.pop()
                word = stack_word + stack_multipilier * word
            else:
                word += char
        
        return word


print(Solution().decodeString("3[a]2[bc]") == "aaabcbc")
print(Solution().decodeString("3[a2[c]]") == "accaccacc")
print(Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef") == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")
print(Solution().decodeString("10[leetcode]") == "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode")