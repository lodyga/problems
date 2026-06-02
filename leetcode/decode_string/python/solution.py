class Solution:
    def decodeString(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack, string
            A: iteration
        """
        stack = []  
        chunk = ""
        multiplier = 0  

        for char in text:
            if char.isdigit():
                multiplier = multiplier*10 + int(char)
            
            elif char == "[":
                stack.append(chunk)
                chunk = ""
                stack.append(multiplier)
                multiplier = 0

            elif char == "]":
                multiplier = stack.pop()
                prev_word = stack.pop()
                chunk = prev_word + multiplier * chunk
                multiplier = 0

            else:
                chunk += char

        return chunk


print(Solution().decodeString("3[a]2[bc]") == "aaabcbc")
print(Solution().decodeString("3[a2[c]]") == "accaccacc")
print(Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
print(Solution().decodeString("10[leetcode]") == "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode")
print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef") == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")
