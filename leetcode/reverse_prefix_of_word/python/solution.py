class Solution:
    def reversePrefix(self, word: str, pivot: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        prefix_list = []
        has_prefix = False

        for index, letter in enumerate(word):
            prefix_list.append(letter)
            if letter == pivot:
                has_prefix = True
                break
        
        if has_prefix:
            prefix = "".join(reversed(prefix_list))
            base = word[index + 1:]
            return prefix + base
        else:
            return word
                

print(Solution().reversePrefix("abcdefd", "d") == "dcbaefd")
print(Solution().reversePrefix("xyxzxe", "z") == "zxyxxe")
print(Solution().reversePrefix("abcd", "z") == "abcd")