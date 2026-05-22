class Solution:
    def isSubsequence(self, sub_seq: str, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        if sub_seq == "":
            return True
        
        idx = 0
        
        for letter in text:
            if sub_seq[idx] == letter:
                idx += 1
                
                if idx == len(sub_seq):
                    return True

        return False


print(Solution().isSubsequence("abc", "ahbgdc") == True)
print(Solution().isSubsequence("axc", "ahbgdc") == False)
print(Solution().isSubsequence("", "ahbgdc") == True)
print(Solution().isSubsequence("", "") == True)
