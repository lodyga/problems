class Solution:
    def decodeString(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        stack = []
        counter = 0
        word = ""

        for char in text:
            if char.isdigit():
                counter = 10 * counter + int(char)
            elif char == "[":
                stack.append(word)
                word = ""
                stack.append(counter)
                counter = 0
            elif char == "]":
                word = stack.pop() * word
                word = stack.pop() + word
            else:
                word += char

        return word


print(Solution().decodeString("3[a]2[bc]") == "aaabcbc")
print(Solution().decodeString("3[a2[c]]") == "accaccacc")
print(Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")
print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef") == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")
print(Solution().decodeString("10[leetcode]") == "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode")